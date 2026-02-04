from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import (
    CONF_COMMAND_TOPIC,
    CONF_FAN_SPEED_LIST,
    CONF_NAME,
    CONF_PAYLOAD_CLEAN_SPOT,
    CONF_PAYLOAD_LOCATE,
    CONF_PAYLOAD_PAUSE,
    CONF_PAYLOAD_RETURN_TO_BASE,
    CONF_PAYLOAD_START,
    CONF_PAYLOAD_STOP,
    CONF_PAYLOAD_TURN_OFF,
    CONF_PAYLOAD_TURN_ON,
    CONF_RETAIN,
    CONF_SEND_COMMAND_TOPIC,
    CONF_SET_FAN_SPEED_TOPIC,
    CONF_STATE_TOPIC,
    CONF_SUPPORTED_FEATURES,
)
from .common import MqttBase, MqttEntityCommon


class Vacuum(MqttEntityCommon, MqttBase):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    command_topic: Annotated[str | None, Field(alias=CONF_COMMAND_TOPIC, min_length=1)] = None
    fan_speed_list: Annotated[list[str] | None, Field(alias=CONF_FAN_SPEED_LIST)] = []
    payload_clean_spot: Annotated[str | None, Field(alias=CONF_PAYLOAD_CLEAN_SPOT)] = "clean_spot"
    payload_locate: Annotated[str | None, Field(alias=CONF_PAYLOAD_LOCATE)] = "locate"
    payload_pause: Annotated[str | None, Field(alias=CONF_PAYLOAD_PAUSE)] = "pause"
    payload_return_to_base: Annotated[str | None, Field(alias=CONF_PAYLOAD_RETURN_TO_BASE)] = "return_to_base"
    payload_start: Annotated[str | None, Field(alias=CONF_PAYLOAD_START)] = "start"
    payload_stop: Annotated[str | None, Field(alias=CONF_PAYLOAD_STOP)] = "stop"
    payload_turn_off: Annotated[str | None, Field(alias=CONF_PAYLOAD_TURN_OFF)] = None
    payload_turn_on: Annotated[str | None, Field(alias=CONF_PAYLOAD_TURN_ON)] = None
    retain: Annotated[bool | None, Field(alias=CONF_RETAIN)] = False
    send_command_topic: Annotated[str | None, Field(alias=CONF_SEND_COMMAND_TOPIC, min_length=1)] = None
    set_fan_speed_topic: Annotated[str | None, Field(alias=CONF_SET_FAN_SPEED_TOPIC, min_length=1)] = None
    state_topic: Annotated[str | None, Field(alias=CONF_STATE_TOPIC, min_length=1)] = None
    supported_features: Annotated[list[str] | None, Field(alias=CONF_SUPPORTED_FEATURES)] = [
        "start",
        "stop",
        "return_home",
        "clean_spot",
    ]
