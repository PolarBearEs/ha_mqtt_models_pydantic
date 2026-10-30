"""MQTT topic validation mirroring Home Assistant's mqtt.util topic validators."""

from __future__ import annotations

from typing import Annotated

from pydantic import AfterValidator


def validate_topic(topic: str) -> str:
    try:
        raw_topic = topic.encode("utf-8")
    except UnicodeError as err:
        raise ValueError("MQTT topic name/filter must be valid UTF-8 string.") from err
    if not raw_topic:
        raise ValueError("MQTT topic name/filter must not be empty.")
    if len(raw_topic) > 65535:
        raise ValueError("MQTT topic name/filter must not be longer than 65535 encoded bytes.")

    for char in topic:
        if char == "\0":
            raise ValueError("MQTT topic name/filter must not contain null character.")
        if char <= "\u001f" or "\u007f" <= char <= "\u009f":
            raise ValueError("MQTT topic name/filter must not contain control characters.")
        if "﷐" <= char <= "﷯" or (ord(char) & 0xFFFF) in (0xFFFE, 0xFFFF):
            raise ValueError("MQTT topic name/filter must not contain non-characters.")

    return topic


def validate_subscribe_topic(topic: str) -> str:
    topic = validate_topic(topic)
    for index, char in enumerate(topic):
        if char == "+" and (
            (index > 0 and topic[index - 1] != "/") or (index < len(topic) - 1 and topic[index + 1] != "/")
        ):
            raise ValueError("Single-level wildcard must occupy an entire level of the filter")

    index = topic.find("#")
    if index != -1:
        if index != len(topic) - 1:
            raise ValueError("Multi-level wildcard must be the last character in the topic filter.")
        if len(topic) > 1 and topic[index - 1] != "/":
            raise ValueError("Multi-level wildcard must be after a topic level separator.")

    return topic


def validate_publish_topic(topic: str) -> str:
    topic = validate_topic(topic)
    if "+" in topic or "#" in topic:
        raise ValueError("Wildcards cannot be used in topic names")
    return topic


PublishTopic = Annotated[str, AfterValidator(validate_publish_topic)]
SubscribeTopic = Annotated[str, AfterValidator(validate_subscribe_topic)]
