from __future__ import annotations

from typing import Annotated

from pydantic import Field, model_validator

from ..const import (
    CONF_ACTION_TEMPLATE,
    CONF_ACTION_TOPIC,
    CONF_COMMAND_TEMPLATE,
    CONF_CURRENT_HUMIDITY_TEMPLATE,
    CONF_CURRENT_HUMIDITY_TOPIC,
    CONF_DEVICE_CLASS,
    CONF_MODE_COMMAND_TEMPLATE,
    CONF_MODE_COMMAND_TOPIC,
    CONF_MODE_LIST,
    CONF_MODE_STATE_TEMPLATE,
    CONF_MODE_STATE_TOPIC,
    CONF_NAME,
    CONF_PAYLOAD_OFF,
    CONF_PAYLOAD_ON,
    CONF_PAYLOAD_RESET_HUMIDITY,
    CONF_PAYLOAD_RESET_MODE,
    CONF_STATE_VALUE_TEMPLATE,
    CONF_TARGET_HUMIDITY_COMMAND_TEMPLATE,
    CONF_TARGET_HUMIDITY_COMMAND_TOPIC,
    CONF_TARGET_HUMIDITY_MAX,
    CONF_TARGET_HUMIDITY_MIN,
    CONF_TARGET_HUMIDITY_STATE_TEMPLATE,
    CONF_TARGET_HUMIDITY_STATE_TOPIC,
    DEFAULT_MAX_HUMIDITY,
    DEFAULT_MIN_HUMIDITY,
    DEFAULT_PAYLOAD_OFF,
    DEFAULT_PAYLOAD_ON,
    DEFAULT_PAYLOAD_RESET,
)
from .common import MqttEntityCommon, MqttReadWrite


class Humidifier(MqttEntityCommon, MqttReadWrite):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    action_template: Annotated[str | None, Field(alias=CONF_ACTION_TEMPLATE)] = None
    action_topic: Annotated[str | None, Field(alias=CONF_ACTION_TOPIC, min_length=1)] = None
    command_template: Annotated[str | None, Field(alias=CONF_COMMAND_TEMPLATE)] = None
    current_humidity_template: Annotated[str | None, Field(alias=CONF_CURRENT_HUMIDITY_TEMPLATE)] = None
    current_humidity_topic: Annotated[str | None, Field(alias=CONF_CURRENT_HUMIDITY_TOPIC, min_length=1)] = None
    device_class: Annotated[str | None, Field(alias=CONF_DEVICE_CLASS)] = "humidifier"
    mode_command_template: Annotated[str | None, Field(alias=CONF_MODE_COMMAND_TEMPLATE)] = None
    mode_command_topic: Annotated[str | None, Field(alias=CONF_MODE_COMMAND_TOPIC, min_length=1)] = None
    mode_state_template: Annotated[str | None, Field(alias=CONF_MODE_STATE_TEMPLATE)] = None
    mode_state_topic: Annotated[str | None, Field(alias=CONF_MODE_STATE_TOPIC, min_length=1)] = None
    modes: Annotated[list[str] | None, Field(alias=CONF_MODE_LIST)] = []
    payload_off: Annotated[str, Field(alias=CONF_PAYLOAD_OFF)] = DEFAULT_PAYLOAD_OFF
    payload_on: Annotated[str, Field(alias=CONF_PAYLOAD_ON)] = DEFAULT_PAYLOAD_ON
    payload_reset_humidity: Annotated[str, Field(alias=CONF_PAYLOAD_RESET_HUMIDITY)] = DEFAULT_PAYLOAD_RESET
    payload_reset_mode: Annotated[str, Field(alias=CONF_PAYLOAD_RESET_MODE)] = DEFAULT_PAYLOAD_RESET
    state_value_template: Annotated[str | None, Field(alias=CONF_STATE_VALUE_TEMPLATE)] = None
    target_humidity_command_template: Annotated[str | None, Field(alias=CONF_TARGET_HUMIDITY_COMMAND_TEMPLATE)] = None
    target_humidity_command_topic: Annotated[str, Field(alias=CONF_TARGET_HUMIDITY_COMMAND_TOPIC, min_length=1)]
    max_humidity: Annotated[float, Field(alias=CONF_TARGET_HUMIDITY_MAX, gt=0)] = DEFAULT_MAX_HUMIDITY
    min_humidity: Annotated[float, Field(alias=CONF_TARGET_HUMIDITY_MIN, gt=0)] = DEFAULT_MIN_HUMIDITY
    target_humidity_state_template: Annotated[str | None, Field(alias=CONF_TARGET_HUMIDITY_STATE_TEMPLATE)] = None
    target_humidity_state_topic: Annotated[str | None, Field(alias=CONF_TARGET_HUMIDITY_STATE_TOPIC, min_length=1)] = (
        None
    )

    @model_validator(mode="after")
    def validate_configuration(self) -> Humidifier:
        if self.min_humidity is not None and self.max_humidity is not None and self.min_humidity >= self.max_humidity:
            raise ValueError("target_humidity_max must be > target_humidity_min")
        if self.max_humidity is not None and self.max_humidity > 100:
            raise ValueError("max_humidity must be <= 100")
        if self.modes and self.mode_command_topic is None:
            raise ValueError("mode_command_topic and modes must be used together")
        if self.modes is not None and self.payload_reset_mode in self.modes:
            raise ValueError("modes must not contain payload_reset_mode")
        return self
