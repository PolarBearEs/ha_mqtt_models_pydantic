from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field, model_validator

from ..const import (
    CONF_COMMAND_TEMPLATE,
    CONF_DEVICE_CLASS,
    CONF_MAX,
    CONF_MIN,
    CONF_MODE,
    CONF_NAME,
    CONF_PAYLOAD_RESET,
    CONF_STEP,
    CONF_UNIT_OF_MEASUREMENT,
    CONF_VALUE_TEMPLATE,
    DEFAULT_PAYLOAD_RESET,
)
from .common import MqttEntityCommon, MqttReadWrite


class NumberMode(StrEnum):
    AUTO = "auto"
    BOX = "box"
    SLIDER = "slider"


class Number(MqttEntityCommon, MqttReadWrite):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    command_template: Annotated[str | None, Field(alias=CONF_COMMAND_TEMPLATE)] = None
    device_class: Annotated[str | None, Field(alias=CONF_DEVICE_CLASS)] = None
    max: Annotated[float, Field(alias=CONF_MAX)] = 100.0
    min: Annotated[float, Field(alias=CONF_MIN)] = 1.0
    mode: Annotated[NumberMode, Field(alias=CONF_MODE)] = NumberMode.AUTO
    payload_reset: Annotated[str, Field(alias=CONF_PAYLOAD_RESET)] = DEFAULT_PAYLOAD_RESET
    step: Annotated[float, Field(alias=CONF_STEP, ge=1e-3)] = 1.0
    unit_of_measurement: Annotated[str | None, Field(alias=CONF_UNIT_OF_MEASUREMENT)] = None
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None

    @model_validator(mode="after")
    def validate_range(self) -> Number:
        if self.min is not None and self.max is not None and self.min > self.max:
            raise ValueError("max must be >= min")
        return self
