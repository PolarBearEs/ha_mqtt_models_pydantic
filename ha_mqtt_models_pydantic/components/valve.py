from __future__ import annotations

from typing import Annotated

from pydantic import Field, model_validator

from ..const import (
    CONF_COMMAND_TEMPLATE,
    CONF_COMMAND_TOPIC,
    CONF_DEVICE_CLASS,
    CONF_NAME,
    CONF_OPTIMISTIC,
    CONF_PAYLOAD_CLOSE,
    CONF_PAYLOAD_OPEN,
    CONF_PAYLOAD_STOP,
    CONF_POSITION_CLOSED,
    CONF_POSITION_OPEN,
    CONF_REPORTS_POSITION,
    CONF_RETAIN,
    CONF_STATE_CLOSED,
    CONF_STATE_CLOSING,
    CONF_STATE_OPEN,
    CONF_STATE_OPENING,
    CONF_STATE_TOPIC,
    CONF_VALUE_TEMPLATE,
    DEFAULT_OPTIMISTIC,
    DEFAULT_PAYLOAD_CLOSE,
    DEFAULT_PAYLOAD_OPEN,
    DEFAULT_POSITION_CLOSED,
    DEFAULT_POSITION_OPEN,
    DEFAULT_RETAIN,
    DEFAULT_STATE_CLOSED,
    DEFAULT_STATE_CLOSING,
    DEFAULT_STATE_OPEN,
    DEFAULT_STATE_OPENING,
)
from .common import MqttBase, MqttEntityCommon


class Valve(MqttEntityCommon, MqttBase):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    command_topic: Annotated[str | None, Field(alias=CONF_COMMAND_TOPIC, min_length=1)] = None
    command_template: Annotated[str | None, Field(alias=CONF_COMMAND_TEMPLATE)] = None
    device_class: Annotated[str | None, Field(alias=CONF_DEVICE_CLASS)] = None
    optimistic: Annotated[bool, Field(alias=CONF_OPTIMISTIC)] = DEFAULT_OPTIMISTIC
    payload_close: Annotated[str | None, Field(alias=CONF_PAYLOAD_CLOSE)] = DEFAULT_PAYLOAD_CLOSE
    payload_open: Annotated[str | None, Field(alias=CONF_PAYLOAD_OPEN)] = DEFAULT_PAYLOAD_OPEN
    payload_stop: Annotated[str | None, Field(alias=CONF_PAYLOAD_STOP)] = None
    position_closed: Annotated[int, Field(alias=CONF_POSITION_CLOSED)] = DEFAULT_POSITION_CLOSED
    position_open: Annotated[int, Field(alias=CONF_POSITION_OPEN)] = DEFAULT_POSITION_OPEN
    reports_position: Annotated[bool, Field(alias=CONF_REPORTS_POSITION)] = False
    retain: Annotated[bool, Field(alias=CONF_RETAIN)] = DEFAULT_RETAIN
    state_closed: Annotated[str, Field(alias=CONF_STATE_CLOSED)] = DEFAULT_STATE_CLOSED
    state_closing: Annotated[str, Field(alias=CONF_STATE_CLOSING)] = DEFAULT_STATE_CLOSING
    state_open: Annotated[str, Field(alias=CONF_STATE_OPEN)] = DEFAULT_STATE_OPEN
    state_opening: Annotated[str, Field(alias=CONF_STATE_OPENING)] = DEFAULT_STATE_OPENING
    state_topic: Annotated[str | None, Field(alias=CONF_STATE_TOPIC, min_length=1)] = None
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None

    @model_validator(mode="after")
    def validate_reports_position(self) -> Valve:
        if self.reports_position and any(
            value is not None and key != "payload_stop"
            for key, value in {
                "payload_open": self.payload_open,
                "payload_close": self.payload_close,
                "state_open": self.state_open,
                "state_closed": self.state_closed,
            }.items()
        ):
            raise ValueError(
                "Options `payload_open`, `payload_close`, `state_open` and `state_closed` "
                "are not allowed if the valve reports a position."
            )
        return self
