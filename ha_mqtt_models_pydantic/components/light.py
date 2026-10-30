from __future__ import annotations

from typing import Annotated

from pydantic import Field, model_validator

from ..const import (
    CONF_BLUE_TEMPLATE,
    CONF_BRIGHTNESS,
    CONF_BRIGHTNESS_COMMAND_TEMPLATE,
    CONF_BRIGHTNESS_COMMAND_TOPIC,
    CONF_BRIGHTNESS_SCALE,
    CONF_BRIGHTNESS_STATE_TOPIC,
    CONF_BRIGHTNESS_TEMPLATE,
    CONF_BRIGHTNESS_VALUE_TEMPLATE,
    CONF_COLOR_MODE_STATE_TOPIC,
    CONF_COLOR_MODE_VALUE_TEMPLATE,
    CONF_COLOR_TEMP_COMMAND_TEMPLATE,
    CONF_COLOR_TEMP_COMMAND_TOPIC,
    CONF_COLOR_TEMP_KELVIN,
    CONF_COLOR_TEMP_STATE_TOPIC,
    CONF_COLOR_TEMP_TEMPLATE,
    CONF_COLOR_TEMP_VALUE_TEMPLATE,
    CONF_COMMAND_OFF_TEMPLATE,
    CONF_COMMAND_ON_TEMPLATE,
    CONF_COMMAND_TOPIC,
    CONF_EFFECT,
    CONF_EFFECT_COMMAND_TEMPLATE,
    CONF_EFFECT_COMMAND_TOPIC,
    CONF_EFFECT_LIST,
    CONF_EFFECT_STATE_TOPIC,
    CONF_EFFECT_TEMPLATE,
    CONF_EFFECT_VALUE_TEMPLATE,
    CONF_FLASH,
    CONF_FLASH_TIME_LONG,
    CONF_FLASH_TIME_SHORT,
    CONF_GREEN_TEMPLATE,
    CONF_HS_COMMAND_TEMPLATE,
    CONF_HS_COMMAND_TOPIC,
    CONF_HS_STATE_TOPIC,
    CONF_HS_VALUE_TEMPLATE,
    CONF_MAX_KELVIN,
    CONF_MAX_MIREDS,
    CONF_MIN_KELVIN,
    CONF_MIN_MIREDS,
    CONF_NAME,
    CONF_ON_COMMAND_TYPE,
    CONF_PAYLOAD_OFF,
    CONF_PAYLOAD_ON,
    CONF_RED_TEMPLATE,
    CONF_RETAIN,
    CONF_RGB_COMMAND_TEMPLATE,
    CONF_RGB_COMMAND_TOPIC,
    CONF_RGB_STATE_TOPIC,
    CONF_RGB_VALUE_TEMPLATE,
    CONF_RGBW_COMMAND_TEMPLATE,
    CONF_RGBW_COMMAND_TOPIC,
    CONF_RGBW_STATE_TOPIC,
    CONF_RGBW_VALUE_TEMPLATE,
    CONF_RGBWW_COMMAND_TEMPLATE,
    CONF_RGBWW_COMMAND_TOPIC,
    CONF_RGBWW_STATE_TOPIC,
    CONF_RGBWW_VALUE_TEMPLATE,
    CONF_SCHEMA,
    CONF_STATE_TEMPLATE,
    CONF_STATE_TOPIC,
    CONF_STATE_VALUE_TEMPLATE,
    CONF_SUPPORTED_COLOR_MODES,
    CONF_TRANSITION,
    CONF_WHITE_COMMAND_TOPIC,
    CONF_WHITE_SCALE,
    CONF_XY_COMMAND_TEMPLATE,
    CONF_XY_COMMAND_TOPIC,
    CONF_XY_STATE_TOPIC,
    CONF_XY_VALUE_TEMPLATE,
    DEFAULT_BRIGHTNESS,
    DEFAULT_BRIGHTNESS_SCALE,
    DEFAULT_EFFECT,
    DEFAULT_FLASH_TIME_LONG,
    DEFAULT_FLASH_TIME_SHORT,
    DEFAULT_ON_COMMAND_TYPE,
    DEFAULT_OPTIMISTIC,
    DEFAULT_PAYLOAD_OFF,
    DEFAULT_PAYLOAD_ON,
    DEFAULT_RETAIN,
    DEFAULT_WHITE_SCALE,
)
from .common import MqttBase, MqttEntityCommon, MqttModel, MqttReadWrite


class _BaseLight(MqttEntityCommon, MqttModel):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    light_schema: Annotated[str | None, Field(alias=CONF_SCHEMA)] = None


class LightJson(_BaseLight, MqttBase):
    brightness: Annotated[bool, Field(alias=CONF_BRIGHTNESS)] = DEFAULT_BRIGHTNESS
    brightness_scale: Annotated[int, Field(alias=CONF_BRIGHTNESS_SCALE, gt=0)] = DEFAULT_BRIGHTNESS_SCALE
    color_temp_kelvin: Annotated[bool, Field(alias=CONF_COLOR_TEMP_KELVIN)] = False
    command_topic: Annotated[str, Field(alias=CONF_COMMAND_TOPIC, min_length=1)]
    effect: Annotated[bool, Field(alias=CONF_EFFECT)] = DEFAULT_EFFECT
    effect_list: Annotated[list[str] | None, Field(alias=CONF_EFFECT_LIST)] = None
    flash: Annotated[bool, Field(alias=CONF_FLASH)] = True
    flash_time_long: Annotated[int, Field(alias=CONF_FLASH_TIME_LONG, gt=0)] = DEFAULT_FLASH_TIME_LONG
    flash_time_short: Annotated[int, Field(alias=CONF_FLASH_TIME_SHORT, gt=0)] = DEFAULT_FLASH_TIME_SHORT
    max_kelvin: Annotated[int | None, Field(alias=CONF_MAX_KELVIN, gt=0)] = None
    max_mireds: Annotated[int | None, Field(alias=CONF_MAX_MIREDS, gt=0)] = None
    min_kelvin: Annotated[int | None, Field(alias=CONF_MIN_KELVIN, gt=0)] = None
    min_mireds: Annotated[int | None, Field(alias=CONF_MIN_MIREDS, gt=0)] = None
    optimistic: Annotated[bool, Field(alias="optimistic")] = DEFAULT_OPTIMISTIC
    retain: Annotated[bool, Field(alias=CONF_RETAIN)] = DEFAULT_RETAIN
    state_topic: Annotated[str | None, Field(alias=CONF_STATE_TOPIC, min_length=1)] = None
    supported_color_modes: Annotated[set[str] | None, Field(alias=CONF_SUPPORTED_COLOR_MODES)] = None
    transition: Annotated[bool, Field(alias=CONF_TRANSITION)] = True
    white_scale: Annotated[int, Field(alias=CONF_WHITE_SCALE, gt=0)] = DEFAULT_WHITE_SCALE
    light_schema: Annotated[str, Field(alias=CONF_SCHEMA)] = "json"


class LightBasic(_BaseLight, MqttReadWrite):
    brightness_command_template: Annotated[str | None, Field(alias=CONF_BRIGHTNESS_COMMAND_TEMPLATE)] = None
    brightness_command_topic: Annotated[str | None, Field(alias=CONF_BRIGHTNESS_COMMAND_TOPIC, min_length=1)] = None
    brightness_scale: Annotated[int, Field(alias=CONF_BRIGHTNESS_SCALE, gt=0)] = DEFAULT_BRIGHTNESS_SCALE
    brightness_state_topic: Annotated[str | None, Field(alias=CONF_BRIGHTNESS_STATE_TOPIC, min_length=1)] = None
    brightness_value_template: Annotated[str | None, Field(alias=CONF_BRIGHTNESS_VALUE_TEMPLATE)] = None
    color_mode_state_topic: Annotated[str | None, Field(alias=CONF_COLOR_MODE_STATE_TOPIC, min_length=1)] = None
    color_mode_value_template: Annotated[str | None, Field(alias=CONF_COLOR_MODE_VALUE_TEMPLATE)] = None
    color_temp_command_template: Annotated[str | None, Field(alias=CONF_COLOR_TEMP_COMMAND_TEMPLATE)] = None
    color_temp_command_topic: Annotated[str | None, Field(alias=CONF_COLOR_TEMP_COMMAND_TOPIC, min_length=1)] = None
    color_temp_kelvin: Annotated[bool, Field(alias=CONF_COLOR_TEMP_KELVIN)] = False
    color_temp_state_topic: Annotated[str | None, Field(alias=CONF_COLOR_TEMP_STATE_TOPIC, min_length=1)] = None
    color_temp_value_template: Annotated[str | None, Field(alias=CONF_COLOR_TEMP_VALUE_TEMPLATE)] = None
    effect_command_template: Annotated[str | None, Field(alias=CONF_EFFECT_COMMAND_TEMPLATE)] = None
    effect_command_topic: Annotated[str | None, Field(alias=CONF_EFFECT_COMMAND_TOPIC, min_length=1)] = None
    effect_list: Annotated[list[str] | None, Field(alias=CONF_EFFECT_LIST)] = None
    effect_state_topic: Annotated[str | None, Field(alias=CONF_EFFECT_STATE_TOPIC, min_length=1)] = None
    effect_value_template: Annotated[str | None, Field(alias=CONF_EFFECT_VALUE_TEMPLATE)] = None
    hs_command_template: Annotated[str | None, Field(alias=CONF_HS_COMMAND_TEMPLATE)] = None
    hs_command_topic: Annotated[str | None, Field(alias=CONF_HS_COMMAND_TOPIC, min_length=1)] = None
    hs_state_topic: Annotated[str | None, Field(alias=CONF_HS_STATE_TOPIC, min_length=1)] = None
    hs_value_template: Annotated[str | None, Field(alias=CONF_HS_VALUE_TEMPLATE)] = None
    max_kelvin: Annotated[int | None, Field(alias=CONF_MAX_KELVIN, gt=0)] = None
    max_mireds: Annotated[int | None, Field(alias=CONF_MAX_MIREDS, gt=0)] = None
    min_kelvin: Annotated[int | None, Field(alias=CONF_MIN_KELVIN, gt=0)] = None
    min_mireds: Annotated[int | None, Field(alias=CONF_MIN_MIREDS, gt=0)] = None
    on_command_type: Annotated[str, Field(alias=CONF_ON_COMMAND_TYPE)] = DEFAULT_ON_COMMAND_TYPE
    payload_off: Annotated[str, Field(alias=CONF_PAYLOAD_OFF)] = DEFAULT_PAYLOAD_OFF
    payload_on: Annotated[str, Field(alias=CONF_PAYLOAD_ON)] = DEFAULT_PAYLOAD_ON
    rgb_command_template: Annotated[str | None, Field(alias=CONF_RGB_COMMAND_TEMPLATE)] = None
    rgb_command_topic: Annotated[str | None, Field(alias=CONF_RGB_COMMAND_TOPIC, min_length=1)] = None
    rgb_state_topic: Annotated[str | None, Field(alias=CONF_RGB_STATE_TOPIC, min_length=1)] = None
    rgb_value_template: Annotated[str | None, Field(alias=CONF_RGB_VALUE_TEMPLATE)] = None
    rgbw_command_template: Annotated[str | None, Field(alias=CONF_RGBW_COMMAND_TEMPLATE)] = None
    rgbw_command_topic: Annotated[str | None, Field(alias=CONF_RGBW_COMMAND_TOPIC, min_length=1)] = None
    rgbw_state_topic: Annotated[str | None, Field(alias=CONF_RGBW_STATE_TOPIC, min_length=1)] = None
    rgbw_value_template: Annotated[str | None, Field(alias=CONF_RGBW_VALUE_TEMPLATE)] = None
    rgbww_command_template: Annotated[str | None, Field(alias=CONF_RGBWW_COMMAND_TEMPLATE)] = None
    rgbww_command_topic: Annotated[str | None, Field(alias=CONF_RGBWW_COMMAND_TOPIC, min_length=1)] = None
    rgbww_state_topic: Annotated[str | None, Field(alias=CONF_RGBWW_STATE_TOPIC, min_length=1)] = None
    rgbww_value_template: Annotated[str | None, Field(alias=CONF_RGBWW_VALUE_TEMPLATE)] = None
    state_value_template: Annotated[str | None, Field(alias=CONF_STATE_VALUE_TEMPLATE)] = None
    white_command_topic: Annotated[str | None, Field(alias=CONF_WHITE_COMMAND_TOPIC, min_length=1)] = None
    white_scale: Annotated[int, Field(alias=CONF_WHITE_SCALE, gt=0)] = DEFAULT_WHITE_SCALE
    xy_command_template: Annotated[str | None, Field(alias=CONF_XY_COMMAND_TEMPLATE)] = None
    xy_command_topic: Annotated[str | None, Field(alias=CONF_XY_COMMAND_TOPIC, min_length=1)] = None
    xy_state_topic: Annotated[str | None, Field(alias=CONF_XY_STATE_TOPIC, min_length=1)] = None
    xy_value_template: Annotated[str | None, Field(alias=CONF_XY_VALUE_TEMPLATE)] = None
    light_schema: Annotated[str, Field(alias=CONF_SCHEMA)] = "basic"


class LightTemplate(_BaseLight, MqttReadWrite):
    blue_template: Annotated[str | None, Field(alias=CONF_BLUE_TEMPLATE)] = None
    brightness_template: Annotated[str | None, Field(alias=CONF_BRIGHTNESS_TEMPLATE)] = None
    color_temp_kelvin: Annotated[bool, Field(alias=CONF_COLOR_TEMP_KELVIN)] = False
    color_temp_template: Annotated[str | None, Field(alias=CONF_COLOR_TEMP_TEMPLATE)] = None
    command_off_template: Annotated[str, Field(alias=CONF_COMMAND_OFF_TEMPLATE)]
    command_on_template: Annotated[str, Field(alias=CONF_COMMAND_ON_TEMPLATE)]
    effect_list: Annotated[list[str] | None, Field(alias=CONF_EFFECT_LIST)] = None
    effect_template: Annotated[str | None, Field(alias=CONF_EFFECT_TEMPLATE)] = None
    green_template: Annotated[str | None, Field(alias=CONF_GREEN_TEMPLATE)] = None
    max_kelvin: Annotated[int | None, Field(alias=CONF_MAX_KELVIN, gt=0)] = None
    max_mireds: Annotated[int | None, Field(alias=CONF_MAX_MIREDS, gt=0)] = None
    min_kelvin: Annotated[int | None, Field(alias=CONF_MIN_KELVIN, gt=0)] = None
    min_mireds: Annotated[int | None, Field(alias=CONF_MIN_MIREDS, gt=0)] = None
    red_template: Annotated[str | None, Field(alias=CONF_RED_TEMPLATE)] = None
    state_template: Annotated[str | None, Field(alias=CONF_STATE_TEMPLATE)] = None
    light_schema: Annotated[str, Field(alias=CONF_SCHEMA)] = "template"

    @model_validator(mode="after")
    def validate_command_templates(self) -> LightTemplate:
        if self.command_topic is None:
            raise ValueError("command_topic is required for template lights")
        return self
