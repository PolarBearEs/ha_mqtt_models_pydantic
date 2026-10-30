from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import CONF_EVENT_TYPES
from .common import DeviceClassBase, MqttEntityCommon, MqttReadOnly


class Event(MqttEntityCommon, DeviceClassBase, MqttReadOnly):
    event_types: Annotated[list[str], Field(alias=CONF_EVENT_TYPES, min_length=1)]
