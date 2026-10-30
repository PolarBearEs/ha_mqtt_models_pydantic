from __future__ import annotations

from typing import Annotated

from pydantic import ConfigDict, Field

from ..const import (
    CONF_DEVICE_CLASS,
    CONF_EXPIRE_AFTER,
    CONF_FORCE_UPDATE,
    CONF_LAST_RESET_VALUE_TEMPLATE,
    CONF_NAME,
    CONF_OPTIONS,
    CONF_STATE_CLASS,
    CONF_SUGGESTED_DISPLAY_PRECISION,
    CONF_UNIT_OF_MEASUREMENT,
)
from .common import MqttEntityCommon, MqttReadOnly


class Sensor(MqttEntityCommon, MqttReadOnly):
    model_config = ConfigDict(populate_by_name=True)

    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    device_class: Annotated[str | None, Field(alias=CONF_DEVICE_CLASS)] = None
    expire_after: Annotated[int | None, Field(gt=0, alias=CONF_EXPIRE_AFTER)] = None
    force_update: Annotated[bool, Field(alias=CONF_FORCE_UPDATE)] = False
    last_reset_value_template: Annotated[str | None, Field(alias=CONF_LAST_RESET_VALUE_TEMPLATE)] = None
    options: Annotated[list[str] | None, Field(alias=CONF_OPTIONS)] = None
    suggested_display_precision: Annotated[int | None, Field(ge=0, alias=CONF_SUGGESTED_DISPLAY_PRECISION)] = None
    state_class: Annotated[str | None, Field(alias=CONF_STATE_CLASS)] = None
    unit_of_measurement: Annotated[str | None, Field(alias=CONF_UNIT_OF_MEASUREMENT)] = None
