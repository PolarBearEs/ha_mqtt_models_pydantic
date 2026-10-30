from __future__ import annotations

from typing import Annotated, Literal

from pydantic import Field

from ..const import (
    CONF_COMMAND_TEMPLATE,
    CONF_COMMAND_TOPIC,
    CONF_NAME,
    CONF_RETAIN,
    CONF_SCHEMA,
    CONF_STATE_TOPIC,
    CONF_VALUE_TEMPLATE,
    DEFAULT_RETAIN,
)
from .common import MqttBase, MqttEntityCommon


class InfraredEmitter(MqttEntityCommon, MqttBase):
    infrared_schema: Annotated[Literal["emitter"], Field(alias=CONF_SCHEMA)]
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    command_template: Annotated[str | None, Field(alias=CONF_COMMAND_TEMPLATE)] = None
    command_topic: Annotated[str, Field(alias=CONF_COMMAND_TOPIC, min_length=1)]
    retain: Annotated[bool, Field(alias=CONF_RETAIN)] = DEFAULT_RETAIN


class InfraredReceiver(MqttEntityCommon, MqttBase):
    infrared_schema: Annotated[Literal["receiver"], Field(alias=CONF_SCHEMA)]
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    state_topic: Annotated[str, Field(alias=CONF_STATE_TOPIC, min_length=1)]
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None
