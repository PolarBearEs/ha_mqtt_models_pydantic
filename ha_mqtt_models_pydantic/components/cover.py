from __future__ import annotations

from typing import Annotated

from pydantic import Field, model_validator

from ..const import (
    CONF_DEVICE_CLASS,
    CONF_GET_POSITION_TEMPLATE,
    CONF_GET_POSITION_TOPIC,
    CONF_NAME,
    CONF_PAYLOAD_CLOSE,
    CONF_PAYLOAD_OPEN,
    CONF_PAYLOAD_STOP,
    CONF_PAYLOAD_STOP_TILT,
    CONF_POSITION_CLOSED,
    CONF_POSITION_OPEN,
    CONF_SET_POSITION_TEMPLATE,
    CONF_SET_POSITION_TOPIC,
    CONF_STATE_CLOSED,
    CONF_STATE_CLOSING,
    CONF_STATE_OPEN,
    CONF_STATE_OPENING,
    CONF_STATE_STOPPED,
    CONF_STATE_TOPIC,
    CONF_TILT_CLOSED_POSITION,
    CONF_TILT_COMMAND_TEMPLATE,
    CONF_TILT_COMMAND_TOPIC,
    CONF_TILT_MAX,
    CONF_TILT_MIN,
    CONF_TILT_OPEN_POSITION,
    CONF_TILT_STATE_OPTIMISTIC,
    CONF_TILT_STATUS_TEMPLATE,
    CONF_TILT_STATUS_TOPIC,
    CONF_VALUE_TEMPLATE,
    DEFAULT_PAYLOAD_CLOSE,
    DEFAULT_PAYLOAD_OPEN,
    DEFAULT_PAYLOAD_STOP,
    DEFAULT_POSITION_CLOSED,
    DEFAULT_POSITION_OPEN,
    DEFAULT_STATE_CLOSED,
    DEFAULT_STATE_CLOSING,
    DEFAULT_STATE_OPEN,
    DEFAULT_STATE_OPENING,
    DEFAULT_STATE_STOPPED,
    DEFAULT_TILT_CLOSED_POSITION,
    DEFAULT_TILT_MAX,
    DEFAULT_TILT_MIN,
    DEFAULT_TILT_OPEN_POSITION,
    DEFAULT_TILT_OPTIMISTIC,
)
from .common import MqttEntityCommon, MqttReadWrite


class Cover(MqttEntityCommon, MqttReadWrite):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    device_class: Annotated[str | None, Field(alias=CONF_DEVICE_CLASS)] = None
    get_position_topic: Annotated[str | None, Field(alias=CONF_GET_POSITION_TOPIC, min_length=1)] = None
    payload_close: Annotated[str | None, Field(alias=CONF_PAYLOAD_CLOSE)] = DEFAULT_PAYLOAD_CLOSE
    payload_open: Annotated[str | None, Field(alias=CONF_PAYLOAD_OPEN)] = DEFAULT_PAYLOAD_OPEN
    payload_stop: Annotated[str | None, Field(alias=CONF_PAYLOAD_STOP)] = DEFAULT_PAYLOAD_STOP
    payload_stop_tilt: Annotated[str | None, Field(alias=CONF_PAYLOAD_STOP_TILT)] = DEFAULT_PAYLOAD_STOP
    position_closed: Annotated[int, Field(alias=CONF_POSITION_CLOSED)] = DEFAULT_POSITION_CLOSED
    position_open: Annotated[int, Field(alias=CONF_POSITION_OPEN)] = DEFAULT_POSITION_OPEN
    set_position_template: Annotated[str | None, Field(alias=CONF_SET_POSITION_TEMPLATE)] = None
    set_position_topic: Annotated[str | None, Field(alias=CONF_SET_POSITION_TOPIC, min_length=1)] = None
    state_closed: Annotated[str, Field(alias=CONF_STATE_CLOSED)] = DEFAULT_STATE_CLOSED
    state_closing: Annotated[str, Field(alias=CONF_STATE_CLOSING)] = DEFAULT_STATE_CLOSING
    state_open: Annotated[str, Field(alias=CONF_STATE_OPEN)] = DEFAULT_STATE_OPEN
    state_opening: Annotated[str, Field(alias=CONF_STATE_OPENING)] = DEFAULT_STATE_OPENING
    state_stopped: Annotated[str, Field(alias=CONF_STATE_STOPPED)] = DEFAULT_STATE_STOPPED
    tilt_closed_value: Annotated[int, Field(alias=CONF_TILT_CLOSED_POSITION)] = DEFAULT_TILT_CLOSED_POSITION
    tilt_command_template: Annotated[str | None, Field(alias=CONF_TILT_COMMAND_TEMPLATE)] = None
    tilt_command_topic: Annotated[str | None, Field(alias=CONF_TILT_COMMAND_TOPIC, min_length=1)] = None
    tilt_max: Annotated[int, Field(alias=CONF_TILT_MAX)] = DEFAULT_TILT_MAX
    tilt_min: Annotated[int, Field(alias=CONF_TILT_MIN)] = DEFAULT_TILT_MIN
    tilt_opened_value: Annotated[int, Field(alias=CONF_TILT_OPEN_POSITION)] = DEFAULT_TILT_OPEN_POSITION
    tilt_optimistic: Annotated[bool, Field(alias=CONF_TILT_STATE_OPTIMISTIC)] = DEFAULT_TILT_OPTIMISTIC
    tilt_status_template: Annotated[str | None, Field(alias=CONF_TILT_STATUS_TEMPLATE)] = None
    tilt_status_topic: Annotated[str | None, Field(alias=CONF_TILT_STATUS_TOPIC, min_length=1)] = None
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None
    position_template: Annotated[str | None, Field(alias=CONF_GET_POSITION_TEMPLATE)] = None

    @model_validator(mode="after")
    def validate_topics(self) -> Cover:
        if self.set_position_topic is not None and self.get_position_topic is None:
            raise ValueError(f"'{CONF_SET_POSITION_TOPIC}' must be set together with '{CONF_GET_POSITION_TOPIC}'.")
        if self.value_template is not None and self.state_topic is None:
            raise ValueError(f"'{CONF_VALUE_TEMPLATE}' must be set together with '{CONF_STATE_TOPIC}'.")
        if self.position_template is not None and self.get_position_topic is None:
            raise ValueError(f"'{CONF_GET_POSITION_TEMPLATE}' must be set together with '{CONF_GET_POSITION_TOPIC}'.")
        if self.set_position_template is not None and self.set_position_topic is None:
            raise ValueError(f"'{CONF_SET_POSITION_TEMPLATE}' must be set together with '{CONF_SET_POSITION_TOPIC}'.")
        if self.tilt_command_template is not None and self.tilt_command_topic is None:
            raise ValueError(f"'{CONF_TILT_COMMAND_TEMPLATE}' must be set together with '{CONF_TILT_COMMAND_TOPIC}'.")
        if self.tilt_status_template is not None and self.tilt_status_topic is None:
            raise ValueError(f"'{CONF_TILT_STATUS_TEMPLATE}' must be set together with '{CONF_TILT_STATUS_TOPIC}'.")
        return self
