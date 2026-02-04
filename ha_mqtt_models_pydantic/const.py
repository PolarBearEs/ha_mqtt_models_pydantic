from __future__ import annotations

from enum import StrEnum
from typing import Final

# Common Home Assistant constants used by the local Pydantic models.
CONF_AUTOMATION_TYPE: Final = "automation_type"
CONF_CODE: Final = "code"
CONF_DEVICE: Final = "device"
CONF_DEVICE_CLASS: Final = "device_class"
CONF_DEVICE_ID: Final = "device_id"
CONF_DOMAIN: Final = "domain"
CONF_ENABLED: Final = "enabled"
CONF_ENTITY_CATEGORY: Final = "entity_category"
CONF_ICON: Final = "icon"
CONF_MODEL: Final = "model"
CONF_MODEL_ID: Final = "model_id"
CONF_NAME: Final = "name"
CONF_OPTIMISTIC: Final = "optimistic"
CONF_PAYLOAD: Final = "payload"
CONF_PAYLOAD_OFF: Final = "payload_off"
CONF_PAYLOAD_ON: Final = "payload_on"
CONF_PLATFORM: Final = "platform"
CONF_STATE: Final = "state"
CONF_STATE_CLASS: Final = "state_class"
CONF_SUBTYPE: Final = "subtype"
CONF_TEMPERATURE_UNIT: Final = "temperature_unit"
CONF_TYPE: Final = "type"
CONF_UNIQUE_ID: Final = "unique_id"
CONF_UNIT_OF_MEASUREMENT: Final = "unit_of_measurement"
CONF_VALUE_TEMPLATE: Final = "value_template"

STATE_ON: Final = "on"
STATE_OFF: Final = "off"
STATE_HOME: Final = "home"
STATE_NOT_HOME: Final = "not_home"
STATE_UNKNOWN: Final = "unknown"
STATE_OPEN: Final = "open"
STATE_OPENING: Final = "opening"
STATE_CLOSED: Final = "closed"
STATE_CLOSING: Final = "closing"
STATE_UNAVAILABLE: Final = "unavailable"


class HVACMode(StrEnum):
    OFF = "off"
    HEAT = "heat"
    COOL = "cool"
    HEAT_COOL = "heat_cool"
    AUTO = "auto"
    DRY = "dry"
    FAN_ONLY = "fan_only"


class HVACAction(StrEnum):
    COOLING = "cooling"
    DEFROSTING = "defrosting"
    DRYING = "drying"
    FAN = "fan"
    HEATING = "heating"
    IDLE = "idle"
    OFF = "off"
    PREHEATING = "preheating"


class FanMode(StrEnum):
    ON = "on"
    OFF = "off"
    AUTO = "auto"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    TOP = "top"
    MIDDLE = "middle"
    FOCUS = "focus"
    DIFFUSE = "diffuse"


class SwingMode(StrEnum):
    ON = "on"
    OFF = "off"
    BOTH = "both"
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"


DEFAULT_MIN_TEMP: Final = 7.0
DEFAULT_MAX_TEMP: Final = 35.0
DEFAULT_MIN_HUMIDITY: Final = 30.0
DEFAULT_MAX_HUMIDITY: Final = 99.0

# MQTT constants mirrored from the vendored Home Assistant source.
AVAILABILITY_ALL: Final = "all"
AVAILABILITY_ANY: Final = "any"
AVAILABILITY_LATEST: Final = "latest"
AVAILABILITY_MODES: Final = [AVAILABILITY_ALL, AVAILABILITY_ANY, AVAILABILITY_LATEST]

CONF_ACTION_TEMPLATE: Final = "action_template"
CONF_ACTION_TOPIC: Final = "action_topic"
CONF_ACTIVITY_STATE_TOPIC: Final = "activity_state_topic"
CONF_ACTIVITY_VALUE_TEMPLATE: Final = "activity_value_template"
CONF_AVAILABLE_TONES: Final = "available_tones"
CONF_AVAILABILITY: Final = "availability"
CONF_AVAILABILITY_MODE: Final = "availability_mode"
CONF_AVAILABILITY_TEMPLATE: Final = "availability_template"
CONF_AVAILABILITY_TOPIC: Final = "availability_topic"
CONF_BIRTH_MESSAGE: Final = "birth_message"
CONF_BLUE_TEMPLATE: Final = "blue_template"
CONF_BRIGHTNESS: Final = "brightness"
CONF_BRIGHTNESS_COMMAND_TEMPLATE: Final = "brightness_command_template"
CONF_BRIGHTNESS_COMMAND_TOPIC: Final = "brightness_command_topic"
CONF_BRIGHTNESS_SCALE: Final = "brightness_scale"
CONF_BRIGHTNESS_STATE_TOPIC: Final = "brightness_state_topic"
CONF_BRIGHTNESS_TEMPLATE: Final = "brightness_template"
CONF_BRIGHTNESS_VALUE_TEMPLATE: Final = "brightness_value_template"
CONF_CODE_ARM_REQUIRED: Final = "code_arm_required"
CONF_CODE_DISARM_REQUIRED: Final = "code_disarm_required"
CONF_CODE_FORMAT: Final = "code_format"
CONF_CODE_TRIGGER_REQUIRED: Final = "code_trigger_required"
CONF_COLOR_MODE_STATE_TOPIC: Final = "color_mode_state_topic"
CONF_COLOR_MODE_VALUE_TEMPLATE: Final = "color_mode_value_template"
CONF_COLOR_TEMP: Final = "color_temp"
CONF_COLOR_TEMP_COMMAND_TEMPLATE: Final = "color_temp_command_template"
CONF_COLOR_TEMP_COMMAND_TOPIC: Final = "color_temp_command_topic"
CONF_COLOR_TEMP_KELVIN: Final = "color_temp_kelvin"
CONF_COLOR_TEMP_STATE_TOPIC: Final = "color_temp_state_topic"
CONF_COLOR_TEMP_TEMPLATE: Final = "color_temp_template"
CONF_COLOR_TEMP_VALUE_TEMPLATE: Final = "color_temp_value_template"
CONF_COMMAND_OFF_TEMPLATE: Final = "command_off_template"
CONF_COMMAND_ON_TEMPLATE: Final = "command_on_template"
CONF_COMMAND_TEMPLATE: Final = "command_template"
CONF_COMMAND_TOPIC: Final = "command_topic"
CONF_COMPONENTS: Final = "components"
CONF_CONFIGURATION_URL: Final = "configuration_url"
CONF_CONNECTIONS: Final = "connections"
CONF_CONTENT_TYPE: Final = "content_type"
CONF_CURRENT_HUMIDITY_TEMPLATE: Final = "current_humidity_template"
CONF_CURRENT_HUMIDITY_TOPIC: Final = "current_humidity_topic"
CONF_CURRENT_TEMP_TEMPLATE: Final = "current_temperature_template"
CONF_CURRENT_TEMP_TOPIC: Final = "current_temperature_topic"
CONF_DEFAULT_ENTITY_ID: Final = "default_entity_id"
CONF_DEPRECATED_VIA_HUB: Final = "via_hub"
CONF_DIRECTION_COMMAND_TEMPLATE: Final = "direction_command_template"
CONF_DIRECTION_COMMAND_TOPIC: Final = "direction_command_topic"
CONF_DIRECTION_STATE_TOPIC: Final = "direction_state_topic"
CONF_DIRECTION_VALUE_TEMPLATE: Final = "direction_value_template"
CONF_DISCOVERY_ID: Final = "discovery_id"
CONF_DISPLAY_PRECISION: Final = "display_precision"
CONF_DOCK_COMMAND_TEMPLATE: Final = "dock_command_template"
CONF_DOCK_COMMAND_TOPIC: Final = "dock_command_topic"
CONF_EFFECT: Final = "effect"
CONF_EFFECT_COMMAND_TEMPLATE: Final = "effect_command_template"
CONF_EFFECT_COMMAND_TOPIC: Final = "effect_command_topic"
CONF_EFFECT_LIST: Final = "effect_list"
CONF_EFFECT_STATE_TOPIC: Final = "effect_state_topic"
CONF_EFFECT_TEMPLATE: Final = "effect_template"
CONF_EFFECT_VALUE_TEMPLATE: Final = "effect_value_template"
CONF_ENABLED_BY_DEFAULT: Final = "enabled_by_default"
CONF_ENCODING: Final = "encoding"
CONF_ENTITY_PICTURE: Final = "entity_picture"
CONF_EVENT_TYPES: Final = "event_types"
CONF_EXPIRE_AFTER: Final = "expire_after"
CONF_FAN_MODE_COMMAND_TEMPLATE: Final = "fan_mode_command_template"
CONF_FAN_MODE_COMMAND_TOPIC: Final = "fan_mode_command_topic"
CONF_FAN_MODE_LIST: Final = "fan_modes"
CONF_FAN_MODE_STATE_TEMPLATE: Final = "fan_mode_state_template"
CONF_FAN_MODE_STATE_TOPIC: Final = "fan_mode_state_topic"
CONF_FAN_SPEED_LIST: Final = "fan_speed_list"
CONF_FLASH: Final = "flash"
CONF_FLASH_TIME_LONG: Final = "flash_time_long"
CONF_FLASH_TIME_SHORT: Final = "flash_time_short"
CONF_FORCE_UPDATE: Final = "force_update"
CONF_GET_POSITION_TEMPLATE: Final = "position_template"
CONF_GET_POSITION_TOPIC: Final = "position_topic"
CONF_GREEN_TEMPLATE: Final = "green_template"
CONF_GROUP: Final = "group"
CONF_HW_VERSION: Final = "hw_version"
CONF_HS_COMMAND_TEMPLATE: Final = "hs_command_template"
CONF_HS_COMMAND_TOPIC: Final = "hs_command_topic"
CONF_HS_STATE_TOPIC: Final = "hs_state_topic"
CONF_HS_VALUE_TEMPLATE: Final = "hs_value_template"
CONF_HUMIDITY_COMMAND_TEMPLATE: Final = "target_humidity_command_template"
CONF_HUMIDITY_COMMAND_TOPIC: Final = "target_humidity_command_topic"
CONF_HUMIDITY_MAX: Final = "max_humidity"
CONF_HUMIDITY_MIN: Final = "min_humidity"
CONF_HUMIDITY_STATE_TEMPLATE: Final = "target_humidity_state_template"
CONF_HUMIDITY_STATE_TOPIC: Final = "target_humidity_state_topic"
CONF_IDENTIFIERS: Final = "identifiers"
CONF_IMAGE_ENCODING: Final = "image_encoding"
CONF_IMAGE_TOPIC: Final = "image_topic"
CONF_JSON_ATTRS_TEMPLATE: Final = "json_attributes_template"
CONF_JSON_ATTRS_TOPIC: Final = "json_attributes_topic"
CONF_LAST_RESET_VALUE_TEMPLATE: Final = "last_reset_value_template"
CONF_LATEST_VERSION_TEMPLATE: Final = "latest_version_template"
CONF_LATEST_VERSION_TOPIC: Final = "latest_version_topic"
CONF_MANUFACTURER: Final = "manufacturer"
CONF_MAX: Final = "max"
CONF_MAX_KELVIN: Final = "max_kelvin"
CONF_MAX_MIREDS: Final = "max_mireds"
CONF_MIN: Final = "min"
CONF_MIN_KELVIN: Final = "min_kelvin"
CONF_MIN_MIREDS: Final = "min_mireds"
CONF_MODE: Final = "mode"
CONF_MODE_COMMAND_TEMPLATE: Final = "mode_command_template"
CONF_MODE_COMMAND_TOPIC: Final = "mode_command_topic"
CONF_MODE_LIST: Final = "modes"
CONF_MODE_STATE_TEMPLATE: Final = "mode_state_template"
CONF_MODE_STATE_TOPIC: Final = "mode_state_topic"
CONF_OBJECT_ID: Final = "object_id"
CONF_OFF_DELAY: Final = "off_delay"
CONF_ON_COMMAND_TYPE: Final = "on_command_type"
CONF_OPTIONS: Final = "options"
CONF_ORIGIN: Final = "origin"
CONF_OSCILLATION_COMMAND_TEMPLATE: Final = "oscillation_command_template"
CONF_OSCILLATION_COMMAND_TOPIC: Final = "oscillation_command_topic"
CONF_OSCILLATION_STATE_TOPIC: Final = "oscillation_state_topic"
CONF_OSCILLATION_VALUE_TEMPLATE: Final = "oscillation_value_template"
CONF_PATTERN: Final = "pattern"
CONF_PAUSE_COMMAND_TEMPLATE: Final = "pause_command_template"
CONF_PAUSE_COMMAND_TOPIC: Final = "pause_command_topic"
CONF_PAYLOAD_ARM_AWAY: Final = "payload_arm_away"
CONF_PAYLOAD_ARM_CUSTOM_BYPASS: Final = "payload_arm_custom_bypass"
CONF_PAYLOAD_ARM_HOME: Final = "payload_arm_home"
CONF_PAYLOAD_ARM_NIGHT: Final = "payload_arm_night"
CONF_PAYLOAD_ARM_VACATION: Final = "payload_arm_vacation"
CONF_PAYLOAD_AVAILABLE: Final = "payload_available"
CONF_PAYLOAD_CLEAN_SPOT: Final = "payload_clean_spot"
CONF_PAYLOAD_CLOSE: Final = "payload_close"
CONF_PAYLOAD_DISARM: Final = "payload_disarm"
CONF_PAYLOAD_HOME: Final = "payload_home"
CONF_PAYLOAD_INSTALL: Final = "payload_install"
CONF_PAYLOAD_LOCATE: Final = "payload_locate"
CONF_PAYLOAD_LOCK: Final = "payload_lock"
CONF_PAYLOAD_NOT_AVAILABLE: Final = "payload_not_available"
CONF_PAYLOAD_NOT_HOME: Final = "payload_not_home"
CONF_PAYLOAD_OSCILLATION_OFF: Final = "payload_oscillation_off"
CONF_PAYLOAD_OSCILLATION_ON: Final = "payload_oscillation_on"
CONF_PAYLOAD_OPEN: Final = "payload_open"
CONF_PAYLOAD_PAUSE: Final = "payload_pause"
CONF_PAYLOAD_PRESS: Final = "payload_press"
CONF_PAYLOAD_RESET: Final = "payload_reset"
CONF_PAYLOAD_RESET_HUMIDITY: Final = "payload_reset_humidity"
CONF_PAYLOAD_RESET_MODE: Final = "payload_reset_mode"
CONF_PAYLOAD_RESET_PERCENTAGE: Final = "payload_reset_percentage"
CONF_PAYLOAD_RESET_PRESET_MODE: Final = "payload_reset_preset_mode"
CONF_PAYLOAD_RETURN_TO_BASE: Final = "payload_return_to_base"
CONF_PAYLOAD_START: Final = "payload_start"
CONF_PAYLOAD_STOP: Final = "payload_stop"
CONF_PAYLOAD_STOP_TILT: Final = "payload_stop_tilt"
CONF_PAYLOAD_TRIGGER: Final = "payload_trigger"
CONF_PAYLOAD_TURN_OFF: Final = "payload_turn_off"
CONF_PAYLOAD_TURN_ON: Final = "payload_turn_on"
CONF_PAYLOAD_UNLOCK: Final = "payload_unlock"
CONF_PERCENTAGE_COMMAND_TEMPLATE: Final = "percentage_command_template"
CONF_PERCENTAGE_COMMAND_TOPIC: Final = "percentage_command_topic"
CONF_PERCENTAGE_STATE_TOPIC: Final = "percentage_state_topic"
CONF_PERCENTAGE_VALUE_TEMPLATE: Final = "percentage_value_template"
CONF_POSITION_CLOSED: Final = "position_closed"
CONF_POSITION_OPEN: Final = "position_open"
CONF_POWER_COMMAND_TEMPLATE: Final = "power_command_template"
CONF_POWER_COMMAND_TOPIC: Final = "power_command_topic"
CONF_PRECISION: Final = "precision"
CONF_PRESET_MODE_COMMAND_TEMPLATE: Final = "preset_mode_command_template"
CONF_PRESET_MODE_COMMAND_TOPIC: Final = "preset_mode_command_topic"
CONF_PRESET_MODE_STATE_TOPIC: Final = "preset_mode_state_topic"
CONF_PRESET_MODE_VALUE_TEMPLATE: Final = "preset_mode_value_template"
CONF_PRESET_MODES_LIST: Final = "preset_modes"
CONF_QOS: Final = "qos"
CONF_RED_TEMPLATE: Final = "red_template"
CONF_RELEASE_SUMMARY: Final = "release_summary"
CONF_RELEASE_URL: Final = "release_url"
CONF_REPORTS_POSITION: Final = "reports_position"
CONF_RETAIN: Final = "retain"
CONF_RGB_COMMAND_TEMPLATE: Final = "rgb_command_template"
CONF_RGB_COMMAND_TOPIC: Final = "rgb_command_topic"
CONF_RGB_STATE_TOPIC: Final = "rgb_state_topic"
CONF_RGB_VALUE_TEMPLATE: Final = "rgb_value_template"
CONF_RGBW_COMMAND_TEMPLATE: Final = "rgbw_command_template"
CONF_RGBW_COMMAND_TOPIC: Final = "rgbw_command_topic"
CONF_RGBW_STATE_TOPIC: Final = "rgbw_state_topic"
CONF_RGBW_VALUE_TEMPLATE: Final = "rgbw_value_template"
CONF_RGBWW_COMMAND_TEMPLATE: Final = "rgbww_command_template"
CONF_RGBWW_COMMAND_TOPIC: Final = "rgbww_command_topic"
CONF_RGBWW_STATE_TOPIC: Final = "rgbww_state_topic"
CONF_RGBWW_VALUE_TEMPLATE: Final = "rgbww_value_template"
CONF_SCHEMA: Final = "schema"
CONF_SEND_COMMAND_TOPIC: Final = "send_command_topic"
CONF_SERIAL_NUMBER: Final = "serial_number"
CONF_SET_FAN_SPEED_TOPIC: Final = "set_fan_speed_topic"
CONF_SET_POSITION_TEMPLATE: Final = "set_position_template"
CONF_SET_POSITION_TOPIC: Final = "set_position_topic"
CONF_SOURCE_TYPE: Final = "source_type"
CONF_SPEED_RANGE_MAX: Final = "speed_range_max"
CONF_SPEED_RANGE_MIN: Final = "speed_range_min"
CONF_START_MOWING_COMMAND_TEMPLATE: Final = "start_mowing_command_template"
CONF_START_MOWING_COMMAND_TOPIC: Final = "start_mowing_command_topic"
CONF_STATE_CLOSED: Final = "state_closed"
CONF_STATE_CLOSING: Final = "state_closing"
CONF_STATE_JAMMED: Final = "state_jammed"
CONF_STATE_LOCKED: Final = "state_locked"
CONF_STATE_LOCKING: Final = "state_locking"
CONF_STATE_OFF: Final = "state_off"
CONF_STATE_ON: Final = "state_on"
CONF_STATE_OPEN: Final = "state_open"
CONF_STATE_OPENING: Final = "state_opening"
CONF_STATE_STOPPED: Final = "state_stopped"
CONF_STATE_TEMPLATE: Final = "state_template"
CONF_STATE_TOPIC: Final = "state_topic"
CONF_STATE_UNLOCKED: Final = "state_unlocked"
CONF_STATE_UNLOCKING: Final = "state_unlocking"
CONF_STATE_VALUE_TEMPLATE: Final = "state_value_template"
CONF_STEP: Final = "step"
CONF_SUGGESTED_AREA: Final = "suggested_area"
CONF_SUGGESTED_DISPLAY_PRECISION: Final = "suggested_display_precision"
CONF_SUPPORTED_COLOR_MODES: Final = "supported_color_modes"
CONF_SUPPORTED_FEATURES: Final = "supported_features"
CONF_SUPPORT_DURATION: Final = "support_duration"
CONF_SUPPORT_URL: Final = "support_url"
CONF_SUPPORT_VOLUME_SET: Final = "support_volume_set"
CONF_SW_VERSION: Final = "sw_version"
CONF_SWING_HORIZONTAL_MODE_COMMAND_TEMPLATE: Final = "swing_horizontal_mode_command_template"
CONF_SWING_HORIZONTAL_MODE_COMMAND_TOPIC: Final = "swing_horizontal_mode_command_topic"
CONF_SWING_HORIZONTAL_MODE_LIST: Final = "swing_horizontal_modes"
CONF_SWING_HORIZONTAL_MODE_STATE_TEMPLATE: Final = "swing_horizontal_mode_state_template"
CONF_SWING_HORIZONTAL_MODE_STATE_TOPIC: Final = "swing_horizontal_mode_state_topic"
CONF_SWING_MODE_COMMAND_TEMPLATE: Final = "swing_mode_command_template"
CONF_SWING_MODE_COMMAND_TOPIC: Final = "swing_mode_command_topic"
CONF_SWING_MODE_LIST: Final = "swing_modes"
CONF_SWING_MODE_STATE_TEMPLATE: Final = "swing_mode_state_template"
CONF_SWING_MODE_STATE_TOPIC: Final = "swing_mode_state_topic"
CONF_TARGET_HUMIDITY_COMMAND_TEMPLATE: Final = CONF_HUMIDITY_COMMAND_TEMPLATE
CONF_TARGET_HUMIDITY_COMMAND_TOPIC: Final = CONF_HUMIDITY_COMMAND_TOPIC
CONF_TARGET_HUMIDITY_MAX: Final = CONF_HUMIDITY_MAX
CONF_TARGET_HUMIDITY_MIN: Final = CONF_HUMIDITY_MIN
CONF_TARGET_HUMIDITY_STATE_TEMPLATE: Final = CONF_HUMIDITY_STATE_TEMPLATE
CONF_TARGET_HUMIDITY_STATE_TOPIC: Final = CONF_HUMIDITY_STATE_TOPIC
CONF_TEMP_COMMAND_TEMPLATE: Final = "temperature_command_template"
CONF_TEMP_COMMAND_TOPIC: Final = "temperature_command_topic"
CONF_TEMP_HIGH_COMMAND_TEMPLATE: Final = "temperature_high_command_template"
CONF_TEMP_HIGH_COMMAND_TOPIC: Final = "temperature_high_command_topic"
CONF_TEMP_HIGH_STATE_TEMPLATE: Final = "temperature_high_state_template"
CONF_TEMP_HIGH_STATE_TOPIC: Final = "temperature_high_state_topic"
CONF_TEMP_INITIAL: Final = "initial"
CONF_TEMP_LOW_COMMAND_TEMPLATE: Final = "temperature_low_command_template"
CONF_TEMP_LOW_COMMAND_TOPIC: Final = "temperature_low_command_topic"
CONF_TEMP_LOW_STATE_TEMPLATE: Final = "temperature_low_state_template"
CONF_TEMP_LOW_STATE_TOPIC: Final = "temperature_low_state_topic"
CONF_TEMP_MAX: Final = "max_temp"
CONF_TEMP_MIN: Final = "min_temp"
CONF_TEMP_STATE_TEMPLATE: Final = "temperature_state_template"
CONF_TEMP_STATE_TOPIC: Final = "temperature_state_topic"
CONF_TEMP_STEP: Final = "temp_step"
CONF_TILT_CLOSED_POSITION: Final = "tilt_closed_value"
CONF_TILT_COMMAND_TEMPLATE: Final = "tilt_command_template"
CONF_TILT_COMMAND_TOPIC: Final = "tilt_command_topic"
CONF_TILT_MAX: Final = "tilt_max"
CONF_TILT_MIN: Final = "tilt_min"
CONF_TILT_OPEN_POSITION: Final = "tilt_opened_value"
CONF_TILT_STATE_OPTIMISTIC: Final = "tilt_optimistic"
CONF_TILT_STATUS_TEMPLATE: Final = "tilt_status_template"
CONF_TILT_STATUS_TOPIC: Final = "tilt_status_topic"
CONF_TITLE: Final = "title"
CONF_TOPIC: Final = "topic"
CONF_TRANSITION: Final = "transition"
CONF_URL_TEMPLATE: Final = "url_template"
CONF_URL_TOPIC: Final = "url_topic"
CONF_VIA_DEVICE: Final = "via_device"
CONF_WHITE_COMMAND_TOPIC: Final = "white_command_topic"
CONF_WHITE_SCALE: Final = "white_scale"
CONF_XY_COMMAND_TEMPLATE: Final = "xy_command_template"
CONF_XY_COMMAND_TOPIC: Final = "xy_command_topic"
CONF_XY_STATE_TOPIC: Final = "xy_state_topic"
CONF_XY_VALUE_TEMPLATE: Final = "xy_value_template"

CONF_TILT_CLOSED_VALUE: Final = CONF_TILT_CLOSED_POSITION
CONF_TILT_OPENED_VALUE: Final = CONF_TILT_OPEN_POSITION
CONF_TILT_OPTIMISTIC: Final = CONF_TILT_STATE_OPTIMISTIC

DEFAULT_ALARM_CONTROL_PANEL_COMMAND_TEMPLATE: Final = "{{action}}"
DEFAULT_BRIGHTNESS: Final = False
DEFAULT_BRIGHTNESS_SCALE: Final = 255
DEFAULT_CLIMATE_INITIAL_TEMPERATURE: Final = 21.0
DEFAULT_EFFECT: Final = False
DEFAULT_ENCODING: Final = "utf-8"
DEFAULT_FLASH_TIME_LONG: Final = 10
DEFAULT_FLASH_TIME_SHORT: Final = 2
DEFAULT_ON_COMMAND_TYPE: Final = "last"
DEFAULT_OPTIMISTIC: Final = False
DEFAULT_PAYLOAD_ARM_AWAY: Final = "ARM_AWAY"
DEFAULT_PAYLOAD_ARM_CUSTOM_BYPASS: Final = "ARM_CUSTOM_BYPASS"
DEFAULT_PAYLOAD_ARM_HOME: Final = "ARM_HOME"
DEFAULT_PAYLOAD_ARM_NIGHT: Final = "ARM_NIGHT"
DEFAULT_PAYLOAD_ARM_VACATION: Final = "ARM_VACATION"
DEFAULT_PAYLOAD_AVAILABLE: Final = "online"
DEFAULT_PAYLOAD_CLOSE: Final = "CLOSE"
DEFAULT_PAYLOAD_DISARM: Final = "DISARM"
DEFAULT_PAYLOAD_HOME: Final = "home"
DEFAULT_PAYLOAD_LOCK: Final = "LOCK"
DEFAULT_PAYLOAD_NOT_AVAILABLE: Final = "offline"
DEFAULT_PAYLOAD_NOT_HOME: Final = "not_home"
DEFAULT_PAYLOAD_OFF: Final = "OFF"
DEFAULT_PAYLOAD_ON: Final = "ON"
DEFAULT_PAYLOAD_OPEN: Final = "OPEN"
DEFAULT_PAYLOAD_OSCILLATE_OFF: Final = "oscillate_off"
DEFAULT_PAYLOAD_OSCILLATE_ON: Final = "oscillate_on"
DEFAULT_PAYLOAD_PRESS: Final = "PRESS"
DEFAULT_PAYLOAD_RESET: Final = "None"
DEFAULT_PAYLOAD_STOP: Final = "STOP"
DEFAULT_PAYLOAD_TRIGGER: Final = "TRIGGER"
DEFAULT_PAYLOAD_UNLOCK: Final = "UNLOCK"
DEFAULT_POSITION_CLOSED: Final = 0
DEFAULT_POSITION_OPEN: Final = 100
DEFAULT_QOS: Final = 0
DEFAULT_RETAIN: Final = False
DEFAULT_SPEED_RANGE_MAX: Final = 100
DEFAULT_SPEED_RANGE_MIN: Final = 1
DEFAULT_STATE_CLOSED: Final = "CLOSED"
DEFAULT_STATE_CLOSING: Final = "CLOSING"
DEFAULT_STATE_JAMMED: Final = "JAMMED"
DEFAULT_STATE_LOCKED: Final = "LOCKED"
DEFAULT_STATE_LOCKING: Final = "LOCKING"
DEFAULT_STATE_OPEN: Final = "OPEN"
DEFAULT_STATE_OPENING: Final = "OPENING"
DEFAULT_STATE_STOPPED: Final = "stopped"
DEFAULT_STATE_UNLOCKED: Final = "UNLOCKED"
DEFAULT_STATE_UNLOCKING: Final = "UNLOCKING"
DEFAULT_TILT_CLOSED_POSITION: Final = 0
DEFAULT_TILT_MAX: Final = 100
DEFAULT_TILT_MIN: Final = 0
DEFAULT_TILT_OPEN_POSITION: Final = 100
DEFAULT_TILT_OPTIMISTIC: Final = False
DEFAULT_WHITE_SCALE: Final = 255

PAYLOAD_EMPTY_JSON: Final = "{}"
PAYLOAD_NONE: Final = "None"
VALUES_ON_COMMAND_TYPE: Final = ["first", "last", "brightness"]

SUPPORTED_COMPONENTS: Final = {
    "alarm_control_panel",
    "binary_sensor",
    "button",
    "camera",
    "climate",
    "cover",
    "device_automation",
    "device_tracker",
    "event",
    "fan",
    "humidifier",
    "image",
    "lawn_mower",
    "light",
    "lock",
    "notify",
    "number",
    "scene",
    "select",
    "sensor",
    "siren",
    "switch",
    "tag",
    "text",
    "update",
    "vacuum",
    "valve",
    "water_heater",
}

ENTITY_PLATFORMS: Final = SUPPORTED_COMPONENTS - {"device_automation", "tag"}
