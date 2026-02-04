from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import (
    CONF_AUTOMATION_TYPE,
    CONF_DEVICE,
    CONF_PAYLOAD,
    CONF_SUBTYPE,
    CONF_TOPIC,
    CONF_TYPE,
    CONF_VALUE_TEMPLATE,
)
from .common import DeviceInfo, MqttBase, MqttModel


class DeviceAutomation(MqttBase, MqttModel):
    automation_type: Annotated[str, Field(alias=CONF_AUTOMATION_TYPE, min_length=1)]
    device: Annotated[DeviceInfo, Field(alias=CONF_DEVICE)]
    payload: Annotated[str | None, Field(alias=CONF_PAYLOAD)] = None
    subtype: Annotated[str, Field(alias=CONF_SUBTYPE, min_length=1)]
    topic: Annotated[str, Field(alias=CONF_TOPIC, min_length=1)]
    type: Annotated[str, Field(alias=CONF_TYPE, min_length=1)]
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None
