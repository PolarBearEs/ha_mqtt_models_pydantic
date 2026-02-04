from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import (
    CONF_ACTIVITY_STATE_TOPIC,
    CONF_ACTIVITY_VALUE_TEMPLATE,
    CONF_DOCK_COMMAND_TEMPLATE,
    CONF_DOCK_COMMAND_TOPIC,
    CONF_NAME,
    CONF_OPTIMISTIC,
    CONF_PAUSE_COMMAND_TEMPLATE,
    CONF_PAUSE_COMMAND_TOPIC,
    CONF_RETAIN,
    CONF_START_MOWING_COMMAND_TEMPLATE,
    CONF_START_MOWING_COMMAND_TOPIC,
    DEFAULT_OPTIMISTIC,
    DEFAULT_RETAIN,
)
from .common import MqttBase, MqttEntityCommon


class LawnMower(MqttEntityCommon, MqttBase):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    activity_state_topic: Annotated[str | None, Field(alias=CONF_ACTIVITY_STATE_TOPIC, min_length=1)] = None
    activity_value_template: Annotated[str | None, Field(alias=CONF_ACTIVITY_VALUE_TEMPLATE)] = None
    dock_command_template: Annotated[str | None, Field(alias=CONF_DOCK_COMMAND_TEMPLATE)] = None
    dock_command_topic: Annotated[str | None, Field(alias=CONF_DOCK_COMMAND_TOPIC, min_length=1)] = None
    optimistic: Annotated[bool | None, Field(alias=CONF_OPTIMISTIC)] = DEFAULT_OPTIMISTIC
    pause_command_template: Annotated[str | None, Field(alias=CONF_PAUSE_COMMAND_TEMPLATE)] = None
    pause_command_topic: Annotated[str | None, Field(alias=CONF_PAUSE_COMMAND_TOPIC, min_length=1)] = None
    retain: Annotated[bool | None, Field(alias=CONF_RETAIN)] = DEFAULT_RETAIN
    start_mowing_command_template: Annotated[str | None, Field(alias=CONF_START_MOWING_COMMAND_TEMPLATE)] = None
    start_mowing_command_topic: Annotated[str | None, Field(alias=CONF_START_MOWING_COMMAND_TOPIC, min_length=1)] = None
