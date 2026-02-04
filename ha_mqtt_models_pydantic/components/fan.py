from __future__ import annotations

from typing import Annotated

from pydantic import Field, model_validator

from ..const import (
    CONF_COMMAND_TEMPLATE,
    CONF_DIRECTION_COMMAND_TEMPLATE,
    CONF_DIRECTION_COMMAND_TOPIC,
    CONF_DIRECTION_STATE_TOPIC,
    CONF_DIRECTION_VALUE_TEMPLATE,
    CONF_NAME,
    CONF_OSCILLATION_COMMAND_TEMPLATE,
    CONF_OSCILLATION_COMMAND_TOPIC,
    CONF_OSCILLATION_STATE_TOPIC,
    CONF_OSCILLATION_VALUE_TEMPLATE,
    CONF_PAYLOAD_OFF,
    CONF_PAYLOAD_ON,
    CONF_PAYLOAD_OSCILLATION_OFF,
    CONF_PAYLOAD_OSCILLATION_ON,
    CONF_PAYLOAD_RESET_PERCENTAGE,
    CONF_PAYLOAD_RESET_PRESET_MODE,
    CONF_PERCENTAGE_COMMAND_TEMPLATE,
    CONF_PERCENTAGE_COMMAND_TOPIC,
    CONF_PERCENTAGE_STATE_TOPIC,
    CONF_PERCENTAGE_VALUE_TEMPLATE,
    CONF_PRESET_MODE_COMMAND_TEMPLATE,
    CONF_PRESET_MODE_COMMAND_TOPIC,
    CONF_PRESET_MODE_STATE_TOPIC,
    CONF_PRESET_MODE_VALUE_TEMPLATE,
    CONF_PRESET_MODES_LIST,
    CONF_SPEED_RANGE_MAX,
    CONF_SPEED_RANGE_MIN,
    CONF_STATE_VALUE_TEMPLATE,
    DEFAULT_PAYLOAD_OFF,
    DEFAULT_PAYLOAD_ON,
    DEFAULT_PAYLOAD_OSCILLATE_OFF,
    DEFAULT_PAYLOAD_OSCILLATE_ON,
    DEFAULT_PAYLOAD_RESET,
    DEFAULT_SPEED_RANGE_MAX,
    DEFAULT_SPEED_RANGE_MIN,
)
from .common import MqttEntityCommon, MqttReadWrite


class Fan(MqttEntityCommon, MqttReadWrite):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    command_template: Annotated[str | None, Field(alias=CONF_COMMAND_TEMPLATE)] = None
    direction_command_topic: Annotated[str | None, Field(alias=CONF_DIRECTION_COMMAND_TOPIC, min_length=1)] = None
    direction_command_template: Annotated[str | None, Field(alias=CONF_DIRECTION_COMMAND_TEMPLATE)] = None
    direction_state_topic: Annotated[str | None, Field(alias=CONF_DIRECTION_STATE_TOPIC, min_length=1)] = None
    direction_value_template: Annotated[str | None, Field(alias=CONF_DIRECTION_VALUE_TEMPLATE)] = None
    oscillation_command_topic: Annotated[str | None, Field(alias=CONF_OSCILLATION_COMMAND_TOPIC, min_length=1)] = None
    oscillation_command_template: Annotated[str | None, Field(alias=CONF_OSCILLATION_COMMAND_TEMPLATE)] = None
    oscillation_state_topic: Annotated[str | None, Field(alias=CONF_OSCILLATION_STATE_TOPIC, min_length=1)] = None
    oscillation_value_template: Annotated[str | None, Field(alias=CONF_OSCILLATION_VALUE_TEMPLATE)] = None
    percentage_command_topic: Annotated[str | None, Field(alias=CONF_PERCENTAGE_COMMAND_TOPIC, min_length=1)] = None
    percentage_command_template: Annotated[str | None, Field(alias=CONF_PERCENTAGE_COMMAND_TEMPLATE)] = None
    percentage_state_topic: Annotated[str | None, Field(alias=CONF_PERCENTAGE_STATE_TOPIC, min_length=1)] = None
    percentage_value_template: Annotated[str | None, Field(alias=CONF_PERCENTAGE_VALUE_TEMPLATE)] = None
    preset_mode_command_topic: Annotated[str | None, Field(alias=CONF_PRESET_MODE_COMMAND_TOPIC, min_length=1)] = None
    preset_modes: Annotated[list[str] | None, Field(alias=CONF_PRESET_MODES_LIST)] = []
    preset_mode_command_template: Annotated[str | None, Field(alias=CONF_PRESET_MODE_COMMAND_TEMPLATE)] = None
    preset_mode_state_topic: Annotated[str | None, Field(alias=CONF_PRESET_MODE_STATE_TOPIC, min_length=1)] = None
    preset_mode_value_template: Annotated[str | None, Field(alias=CONF_PRESET_MODE_VALUE_TEMPLATE)] = None
    speed_range_min: Annotated[int | None, Field(alias=CONF_SPEED_RANGE_MIN, gt=0)] = DEFAULT_SPEED_RANGE_MIN
    speed_range_max: Annotated[int | None, Field(alias=CONF_SPEED_RANGE_MAX, gt=0)] = DEFAULT_SPEED_RANGE_MAX
    payload_reset_percentage: Annotated[str | None, Field(alias=CONF_PAYLOAD_RESET_PERCENTAGE)] = DEFAULT_PAYLOAD_RESET
    payload_reset_preset_mode: Annotated[str | None, Field(alias=CONF_PAYLOAD_RESET_PRESET_MODE)] = (
        DEFAULT_PAYLOAD_RESET
    )
    payload_off: Annotated[str | None, Field(alias=CONF_PAYLOAD_OFF)] = DEFAULT_PAYLOAD_OFF
    payload_on: Annotated[str | None, Field(alias=CONF_PAYLOAD_ON)] = DEFAULT_PAYLOAD_ON
    payload_oscillation_off: Annotated[str | None, Field(alias=CONF_PAYLOAD_OSCILLATION_OFF)] = (
        DEFAULT_PAYLOAD_OSCILLATE_OFF
    )
    payload_oscillation_on: Annotated[str | None, Field(alias=CONF_PAYLOAD_OSCILLATION_ON)] = (
        DEFAULT_PAYLOAD_OSCILLATE_ON
    )
    state_value_template: Annotated[str | None, Field(alias=CONF_STATE_VALUE_TEMPLATE)] = None

    @model_validator(mode="after")
    def validate_configuration(self) -> Fan:
        if (
            self.speed_range_min is not None
            and self.speed_range_max is not None
            and self.speed_range_min >= self.speed_range_max
        ):
            raise ValueError("speed_range_max must be > speed_range_min")
        if self.preset_modes and self.payload_reset_preset_mode in self.preset_modes:
            raise ValueError("preset_modes must not contain payload_reset_preset_mode")
        if self.preset_modes and self.preset_mode_command_topic is None:
            raise ValueError("preset_mode_command_topic and preset_modes must be used together")
        if self.preset_mode_command_topic is not None and not self.preset_modes:
            raise ValueError("preset_mode_command_topic and preset_modes must be used together")
        return self
