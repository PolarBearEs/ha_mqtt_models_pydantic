from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import (
    CONF_CURRENT_TEMP_TEMPLATE,
    CONF_CURRENT_TEMP_TOPIC,
    CONF_MODE_COMMAND_TEMPLATE,
    CONF_MODE_COMMAND_TOPIC,
    CONF_MODE_LIST,
    CONF_MODE_STATE_TEMPLATE,
    CONF_MODE_STATE_TOPIC,
    CONF_NAME,
    CONF_OPTIMISTIC,
    CONF_PAYLOAD_OFF,
    CONF_PAYLOAD_ON,
    CONF_POWER_COMMAND_TEMPLATE,
    CONF_POWER_COMMAND_TOPIC,
    CONF_PRECISION,
    CONF_RETAIN,
    CONF_TEMP_COMMAND_TEMPLATE,
    CONF_TEMP_COMMAND_TOPIC,
    CONF_TEMP_INITIAL,
    CONF_TEMP_MAX,
    CONF_TEMP_MIN,
    CONF_TEMP_STATE_TEMPLATE,
    CONF_TEMP_STATE_TOPIC,
    CONF_TEMPERATURE_UNIT,
    CONF_VALUE_TEMPLATE,
    DEFAULT_OPTIMISTIC,
    DEFAULT_RETAIN,
)
from .common import MqttBase, MqttEntityCommon


class WaterHeater(MqttEntityCommon, MqttBase):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    current_temperature_template: Annotated[str | None, Field(alias=CONF_CURRENT_TEMP_TEMPLATE)] = None
    current_temperature_topic: Annotated[str | None, Field(alias=CONF_CURRENT_TEMP_TOPIC, min_length=1)] = None
    mode_command_template: Annotated[str | None, Field(alias=CONF_MODE_COMMAND_TEMPLATE)] = None
    mode_command_topic: Annotated[str | None, Field(alias=CONF_MODE_COMMAND_TOPIC, min_length=1)] = None
    mode_state_template: Annotated[str | None, Field(alias=CONF_MODE_STATE_TEMPLATE)] = None
    mode_state_topic: Annotated[str | None, Field(alias=CONF_MODE_STATE_TOPIC, min_length=1)] = None
    modes: Annotated[list[str] | None, Field(alias=CONF_MODE_LIST)] = [
        "eco",
        "electric",
        "gas",
        "heat_pump",
        "high_demand",
        "performance",
        "off",
    ]
    optimistic: Annotated[bool | None, Field(alias=CONF_OPTIMISTIC)] = DEFAULT_OPTIMISTIC
    payload_off: Annotated[str | None, Field(alias=CONF_PAYLOAD_OFF)] = "OFF"
    payload_on: Annotated[str | None, Field(alias=CONF_PAYLOAD_ON)] = "ON"
    power_command_topic: Annotated[str | None, Field(alias=CONF_POWER_COMMAND_TOPIC, min_length=1)] = None
    power_command_template: Annotated[str | None, Field(alias=CONF_POWER_COMMAND_TEMPLATE)] = None
    precision: Annotated[float | None, Field(alias=CONF_PRECISION)] = None
    retain: Annotated[bool | None, Field(alias=CONF_RETAIN)] = DEFAULT_RETAIN
    initial: Annotated[float | None, Field(alias=CONF_TEMP_INITIAL)] = None
    min_temp: Annotated[float | None, Field(alias=CONF_TEMP_MIN)] = None
    max_temp: Annotated[float | None, Field(alias=CONF_TEMP_MAX)] = None
    temperature_command_template: Annotated[str | None, Field(alias=CONF_TEMP_COMMAND_TEMPLATE)] = None
    temperature_command_topic: Annotated[str | None, Field(alias=CONF_TEMP_COMMAND_TOPIC, min_length=1)] = None
    temperature_state_template: Annotated[str | None, Field(alias=CONF_TEMP_STATE_TEMPLATE)] = None
    temperature_state_topic: Annotated[str | None, Field(alias=CONF_TEMP_STATE_TOPIC, min_length=1)] = None
    temperature_unit: Annotated[str | None, Field(alias=CONF_TEMPERATURE_UNIT)] = None
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None
