from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import CONF_DEVICE, CONF_TOPIC, CONF_VALUE_TEMPLATE
from .common import DeviceInfo, MqttBase, MqttModel


class Tag(MqttBase, MqttModel):
    device: Annotated[DeviceInfo | None, Field(alias=CONF_DEVICE)] = None
    topic: Annotated[str, Field(alias=CONF_TOPIC, min_length=1)]
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None
