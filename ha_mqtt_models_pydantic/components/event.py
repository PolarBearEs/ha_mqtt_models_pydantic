from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import CONF_DEVICE_CLASS, CONF_EVENT_TYPES, CONF_NAME
from .common import MqttEntityCommon, MqttReadOnly


class Event(MqttEntityCommon, MqttReadOnly):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    device_class: Annotated[str | None, Field(alias=CONF_DEVICE_CLASS)] = None
    event_types: Annotated[list[str], Field(alias=CONF_EVENT_TYPES, min_length=1)]
