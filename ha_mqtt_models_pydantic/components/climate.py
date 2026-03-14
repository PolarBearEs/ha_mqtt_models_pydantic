from __future__ import annotations

from typing import Annotated

from pydantic import Field, model_validator

from ..const import (
    CONF_ACTION_TEMPLATE,
    CONF_ACTION_TOPIC,
    CONF_CURRENT_HUMIDITY_TEMPLATE,
    CONF_CURRENT_HUMIDITY_TOPIC,
    CONF_CURRENT_TEMP_TEMPLATE,
    CONF_CURRENT_TEMP_TOPIC,
    CONF_FAN_MODE_COMMAND_TEMPLATE,
    CONF_FAN_MODE_COMMAND_TOPIC,
    CONF_FAN_MODE_LIST,
    CONF_FAN_MODE_STATE_TEMPLATE,
    CONF_FAN_MODE_STATE_TOPIC,
    CONF_HUMIDITY_MAX,
    CONF_HUMIDITY_MIN,
    CONF_MODE_COMMAND_TEMPLATE,
    CONF_MODE_COMMAND_TOPIC,
    CONF_MODE_LIST,
    CONF_MODE_STATE_TEMPLATE,
    CONF_MODE_STATE_TOPIC,
    CONF_NAME,
    CONF_PAYLOAD_OFF,
    CONF_PAYLOAD_ON,
    CONF_POWER_COMMAND_TEMPLATE,
    CONF_POWER_COMMAND_TOPIC,
    CONF_PRECISION,
    CONF_PRESET_MODE_COMMAND_TEMPLATE,
    CONF_PRESET_MODE_COMMAND_TOPIC,
    CONF_PRESET_MODE_STATE_TOPIC,
    CONF_PRESET_MODE_VALUE_TEMPLATE,
    CONF_PRESET_MODES_LIST,
    CONF_SWING_HORIZONTAL_MODE_COMMAND_TEMPLATE,
    CONF_SWING_HORIZONTAL_MODE_COMMAND_TOPIC,
    CONF_SWING_HORIZONTAL_MODE_LIST,
    CONF_SWING_HORIZONTAL_MODE_STATE_TEMPLATE,
    CONF_SWING_HORIZONTAL_MODE_STATE_TOPIC,
    CONF_SWING_MODE_COMMAND_TEMPLATE,
    CONF_SWING_MODE_COMMAND_TOPIC,
    CONF_SWING_MODE_LIST,
    CONF_SWING_MODE_STATE_TEMPLATE,
    CONF_SWING_MODE_STATE_TOPIC,
    CONF_TARGET_HUMIDITY_COMMAND_TEMPLATE,
    CONF_TARGET_HUMIDITY_COMMAND_TOPIC,
    CONF_TARGET_HUMIDITY_STATE_TEMPLATE,
    CONF_TARGET_HUMIDITY_STATE_TOPIC,
    CONF_TEMP_COMMAND_TEMPLATE,
    CONF_TEMP_COMMAND_TOPIC,
    CONF_TEMP_HIGH_COMMAND_TEMPLATE,
    CONF_TEMP_HIGH_COMMAND_TOPIC,
    CONF_TEMP_HIGH_STATE_TEMPLATE,
    CONF_TEMP_HIGH_STATE_TOPIC,
    CONF_TEMP_INITIAL,
    CONF_TEMP_LOW_COMMAND_TEMPLATE,
    CONF_TEMP_LOW_COMMAND_TOPIC,
    CONF_TEMP_LOW_STATE_TEMPLATE,
    CONF_TEMP_LOW_STATE_TOPIC,
    CONF_TEMP_MAX,
    CONF_TEMP_MIN,
    CONF_TEMP_STATE_TEMPLATE,
    CONF_TEMP_STATE_TOPIC,
    CONF_TEMP_STEP,
    CONF_TEMPERATURE_UNIT,
    CONF_VALUE_TEMPLATE,
    DEFAULT_CLIMATE_INITIAL_TEMPERATURE,
    DEFAULT_MAX_HUMIDITY,
    DEFAULT_MAX_TEMP,
    DEFAULT_MIN_HUMIDITY,
    DEFAULT_MIN_TEMP,
    DEFAULT_PAYLOAD_OFF,
    DEFAULT_PAYLOAD_ON,
    FanMode,
    HVACMode,
    SwingMode,
)
from .common import MqttEntityCommon, MqttReadWrite


class Climate(MqttEntityCommon, MqttReadWrite):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    action_template: Annotated[str | None, Field(alias=CONF_ACTION_TEMPLATE)] = None
    action_topic: Annotated[str | None, Field(alias=CONF_ACTION_TOPIC, min_length=1)] = None
    current_humidity_template: Annotated[str | None, Field(alias=CONF_CURRENT_HUMIDITY_TEMPLATE)] = None
    current_humidity_topic: Annotated[str | None, Field(alias=CONF_CURRENT_HUMIDITY_TOPIC, min_length=1)] = None
    current_temperature_template: Annotated[str | None, Field(alias=CONF_CURRENT_TEMP_TEMPLATE)] = None
    current_temperature_topic: Annotated[str | None, Field(alias=CONF_CURRENT_TEMP_TOPIC, min_length=1)] = None
    fan_mode_command_template: Annotated[str | None, Field(alias=CONF_FAN_MODE_COMMAND_TEMPLATE)] = None
    fan_mode_command_topic: Annotated[str | None, Field(alias=CONF_FAN_MODE_COMMAND_TOPIC, min_length=1)] = None
    fan_modes: Annotated[list[str] | None, Field(alias=CONF_FAN_MODE_LIST)] = [
        FanMode.AUTO,
        FanMode.LOW,
        FanMode.MEDIUM,
        FanMode.HIGH,
    ]
    fan_mode_state_template: Annotated[str | None, Field(alias=CONF_FAN_MODE_STATE_TEMPLATE)] = None
    fan_mode_state_topic: Annotated[str | None, Field(alias=CONF_FAN_MODE_STATE_TOPIC, min_length=1)] = None
    target_humidity_command_template: Annotated[str | None, Field(alias=CONF_TARGET_HUMIDITY_COMMAND_TEMPLATE)] = None
    target_humidity_command_topic: Annotated[
        str | None, Field(alias=CONF_TARGET_HUMIDITY_COMMAND_TOPIC, min_length=1)
    ] = None
    max_humidity: Annotated[float, Field(alias=CONF_HUMIDITY_MAX, gt=0)] = DEFAULT_MAX_HUMIDITY
    min_humidity: Annotated[float, Field(alias=CONF_HUMIDITY_MIN, gt=0)] = DEFAULT_MIN_HUMIDITY
    target_humidity_state_template: Annotated[str | None, Field(alias=CONF_TARGET_HUMIDITY_STATE_TEMPLATE)] = None
    target_humidity_state_topic: Annotated[str | None, Field(alias=CONF_TARGET_HUMIDITY_STATE_TOPIC, min_length=1)] = (
        None
    )
    mode_command_template: Annotated[str | None, Field(alias=CONF_MODE_COMMAND_TEMPLATE)] = None
    mode_command_topic: Annotated[str | None, Field(alias=CONF_MODE_COMMAND_TOPIC, min_length=1)] = None
    modes: Annotated[list[str] | None, Field(alias=CONF_MODE_LIST)] = [
        HVACMode.AUTO,
        HVACMode.OFF,
        HVACMode.COOL,
        HVACMode.HEAT,
        HVACMode.DRY,
        HVACMode.FAN_ONLY,
    ]
    mode_state_template: Annotated[str | None, Field(alias=CONF_MODE_STATE_TEMPLATE)] = None
    mode_state_topic: Annotated[str | None, Field(alias=CONF_MODE_STATE_TOPIC, min_length=1)] = None
    payload_on: Annotated[str, Field(alias=CONF_PAYLOAD_ON)] = DEFAULT_PAYLOAD_ON
    payload_off: Annotated[str, Field(alias=CONF_PAYLOAD_OFF)] = DEFAULT_PAYLOAD_OFF
    power_command_topic: Annotated[str | None, Field(alias=CONF_POWER_COMMAND_TOPIC, min_length=1)] = None
    power_command_template: Annotated[str | None, Field(alias=CONF_POWER_COMMAND_TEMPLATE)] = None
    precision: Annotated[float | None, Field(alias=CONF_PRECISION)] = None
    preset_mode_command_topic: Annotated[str | None, Field(alias=CONF_PRESET_MODE_COMMAND_TOPIC, min_length=1)] = None
    preset_mode_command_template: Annotated[str | None, Field(alias=CONF_PRESET_MODE_COMMAND_TEMPLATE)] = None
    preset_mode_state_topic: Annotated[str | None, Field(alias=CONF_PRESET_MODE_STATE_TOPIC, min_length=1)] = None
    preset_mode_value_template: Annotated[str | None, Field(alias=CONF_PRESET_MODE_VALUE_TEMPLATE)] = None
    preset_modes: Annotated[list[str] | None, Field(alias=CONF_PRESET_MODES_LIST)] = []
    swing_horizontal_mode_command_template: Annotated[
        str | None, Field(alias=CONF_SWING_HORIZONTAL_MODE_COMMAND_TEMPLATE)
    ] = None
    swing_horizontal_mode_command_topic: Annotated[
        str | None, Field(alias=CONF_SWING_HORIZONTAL_MODE_COMMAND_TOPIC, min_length=1)
    ] = None
    swing_horizontal_modes: Annotated[list[str] | None, Field(alias=CONF_SWING_HORIZONTAL_MODE_LIST)] = [
        SwingMode.ON,
        SwingMode.OFF,
    ]
    swing_horizontal_mode_state_template: Annotated[
        str | None, Field(alias=CONF_SWING_HORIZONTAL_MODE_STATE_TEMPLATE)
    ] = None
    swing_horizontal_mode_state_topic: Annotated[
        str | None, Field(alias=CONF_SWING_HORIZONTAL_MODE_STATE_TOPIC, min_length=1)
    ] = None
    swing_mode_command_template: Annotated[str | None, Field(alias=CONF_SWING_MODE_COMMAND_TEMPLATE)] = None
    swing_mode_command_topic: Annotated[str | None, Field(alias=CONF_SWING_MODE_COMMAND_TOPIC, min_length=1)] = None
    swing_modes: Annotated[list[str] | None, Field(alias=CONF_SWING_MODE_LIST)] = [SwingMode.ON, SwingMode.OFF]
    swing_mode_state_template: Annotated[str | None, Field(alias=CONF_SWING_MODE_STATE_TEMPLATE)] = None
    swing_mode_state_topic: Annotated[str | None, Field(alias=CONF_SWING_MODE_STATE_TOPIC, min_length=1)] = None
    initial: Annotated[float, Field(alias=CONF_TEMP_INITIAL)] = DEFAULT_CLIMATE_INITIAL_TEMPERATURE
    min_temp: Annotated[float, Field(alias=CONF_TEMP_MIN)] = DEFAULT_MIN_TEMP
    max_temp: Annotated[float, Field(alias=CONF_TEMP_MAX)] = DEFAULT_MAX_TEMP
    temp_step: Annotated[float, Field(alias=CONF_TEMP_STEP)] = 1.0
    temperature_command_template: Annotated[str | None, Field(alias=CONF_TEMP_COMMAND_TEMPLATE)] = None
    temperature_command_topic: Annotated[str | None, Field(alias=CONF_TEMP_COMMAND_TOPIC, min_length=1)] = None
    temperature_high_command_template: Annotated[str | None, Field(alias=CONF_TEMP_HIGH_COMMAND_TEMPLATE)] = None
    temperature_high_command_topic: Annotated[str | None, Field(alias=CONF_TEMP_HIGH_COMMAND_TOPIC, min_length=1)] = (
        None
    )
    temperature_high_state_template: Annotated[str | None, Field(alias=CONF_TEMP_HIGH_STATE_TEMPLATE)] = None
    temperature_high_state_topic: Annotated[str | None, Field(alias=CONF_TEMP_HIGH_STATE_TOPIC, min_length=1)] = None
    temperature_low_command_template: Annotated[str | None, Field(alias=CONF_TEMP_LOW_COMMAND_TEMPLATE)] = None
    temperature_low_command_topic: Annotated[str | None, Field(alias=CONF_TEMP_LOW_COMMAND_TOPIC, min_length=1)] = None
    temperature_low_state_template: Annotated[str | None, Field(alias=CONF_TEMP_LOW_STATE_TEMPLATE)] = None
    temperature_low_state_topic: Annotated[str | None, Field(alias=CONF_TEMP_LOW_STATE_TOPIC, min_length=1)] = None
    temperature_state_template: Annotated[str | None, Field(alias=CONF_TEMP_STATE_TEMPLATE)] = None
    temperature_state_topic: Annotated[str | None, Field(alias=CONF_TEMP_STATE_TOPIC, min_length=1)] = None
    temperature_unit: Annotated[str | None, Field(alias=CONF_TEMPERATURE_UNIT)] = None
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None

    @model_validator(mode="after")
    def validate_configuration(self) -> Climate:
        if self.preset_modes and "none" in self.preset_modes:
            raise ValueError("preset_modes must not include preset mode 'none'")
        if self.min_humidity is not None and self.max_humidity is not None and self.min_humidity >= self.max_humidity:
            raise ValueError("target_humidity_max must be > target_humidity_min")
        if self.max_humidity is not None and self.max_humidity > 100:
            raise ValueError("max_humidity must be <= 100")
        if self.target_humidity_state_topic is not None and self.target_humidity_command_topic is None:
            raise ValueError(
                f"{CONF_TARGET_HUMIDITY_STATE_TOPIC} cannot be used without {CONF_TARGET_HUMIDITY_COMMAND_TOPIC}"
            )
        if self.preset_modes and self.preset_mode_command_topic is None:
            raise ValueError("preset_mode_command_topic and preset_modes must be used together")
        return self
