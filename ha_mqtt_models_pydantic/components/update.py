from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import (
    CONF_COMMAND_TOPIC,
    CONF_DEVICE_CLASS,
    CONF_DISPLAY_PRECISION,
    CONF_LATEST_VERSION_TEMPLATE,
    CONF_LATEST_VERSION_TOPIC,
    CONF_NAME,
    CONF_PAYLOAD_INSTALL,
    CONF_RELEASE_SUMMARY,
    CONF_RELEASE_URL,
    CONF_RETAIN,
    CONF_STATE_TOPIC,
    CONF_TITLE,
    CONF_VALUE_TEMPLATE,
    DEFAULT_RETAIN,
)
from .common import MqttBase, MqttEntityCommon, PreservedUrl


class Update(MqttEntityCommon, MqttBase):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    command_topic: Annotated[str | None, Field(alias=CONF_COMMAND_TOPIC, min_length=1)] = None
    device_class: Annotated[str | None, Field(alias=CONF_DEVICE_CLASS)] = None
    display_precision: Annotated[int | None, Field(alias=CONF_DISPLAY_PRECISION, ge=0)] = 0
    latest_version_template: Annotated[str | None, Field(alias=CONF_LATEST_VERSION_TEMPLATE)] = None
    latest_version_topic: Annotated[str | None, Field(alias=CONF_LATEST_VERSION_TOPIC, min_length=1)] = None
    payload_install: Annotated[str | None, Field(alias=CONF_PAYLOAD_INSTALL)] = None
    release_summary: Annotated[str | None, Field(alias=CONF_RELEASE_SUMMARY)] = None
    release_url: Annotated[PreservedUrl | None, Field(alias=CONF_RELEASE_URL)] = None
    retain: Annotated[bool | None, Field(alias=CONF_RETAIN)] = DEFAULT_RETAIN
    state_topic: Annotated[str | None, Field(alias=CONF_STATE_TOPIC, min_length=1)] = None
    title: Annotated[str | None, Field(alias=CONF_TITLE)] = None
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None
