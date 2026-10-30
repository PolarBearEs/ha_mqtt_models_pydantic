from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import (
    CONF_AVAILABLE_TONES,
    CONF_COMMAND_OFF_TEMPLATE,
    CONF_COMMAND_TEMPLATE,
    CONF_NAME,
    CONF_PAYLOAD_OFF,
    CONF_PAYLOAD_ON,
    CONF_STATE_OFF,
    CONF_STATE_ON,
    CONF_STATE_VALUE_TEMPLATE,
    CONF_SUPPORT_DURATION,
    CONF_SUPPORT_VOLUME_SET,
    DEFAULT_PAYLOAD_OFF,
    DEFAULT_PAYLOAD_ON,
)
from .common import MqttEntityCommon, MqttReadWrite


class Siren(MqttEntityCommon, MqttReadWrite):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    available_tones: Annotated[list[str] | None, Field(alias=CONF_AVAILABLE_TONES)] = None
    command_off_template: Annotated[str | None, Field(alias=CONF_COMMAND_OFF_TEMPLATE)] = None
    command_template: Annotated[str | None, Field(alias=CONF_COMMAND_TEMPLATE)] = None
    payload_off: Annotated[str, Field(alias=CONF_PAYLOAD_OFF)] = DEFAULT_PAYLOAD_OFF
    payload_on: Annotated[str, Field(alias=CONF_PAYLOAD_ON)] = DEFAULT_PAYLOAD_ON
    state_off: Annotated[str | None, Field(alias=CONF_STATE_OFF)] = None
    state_on: Annotated[str | None, Field(alias=CONF_STATE_ON)] = None
    state_value_template: Annotated[str | None, Field(alias=CONF_STATE_VALUE_TEMPLATE)] = None
    support_duration: Annotated[bool, Field(alias=CONF_SUPPORT_DURATION)] = True
    support_volume_set: Annotated[bool, Field(alias=CONF_SUPPORT_VOLUME_SET)] = True
