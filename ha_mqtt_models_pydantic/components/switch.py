from __future__ import annotations

from typing import Annotated

from pydantic import ConfigDict, Field

from ..const import (
    CONF_COMMAND_TEMPLATE,
    CONF_DEVICE_CLASS,
    CONF_NAME,
    CONF_PAYLOAD_OFF,
    CONF_PAYLOAD_ON,
    CONF_STATE_OFF,
    CONF_STATE_ON,
    CONF_VALUE_TEMPLATE,
    DEFAULT_PAYLOAD_OFF,
    DEFAULT_PAYLOAD_ON,
)
from .common import MqttEntityCommon, MqttReadWrite


class Switch(MqttEntityCommon, MqttReadWrite):
    model_config = ConfigDict(populate_by_name=True)

    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    command_template: Annotated[str | None, Field(alias=CONF_COMMAND_TEMPLATE)] = None
    device_class: Annotated[str | None, Field(alias=CONF_DEVICE_CLASS)] = None
    payload_off: Annotated[str, Field(alias=CONF_PAYLOAD_OFF)] = DEFAULT_PAYLOAD_OFF
    payload_on: Annotated[str, Field(alias=CONF_PAYLOAD_ON)] = DEFAULT_PAYLOAD_ON
    state_off: Annotated[str | None, Field(alias=CONF_STATE_OFF)] = None
    state_on: Annotated[str | None, Field(alias=CONF_STATE_ON)] = None
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None
