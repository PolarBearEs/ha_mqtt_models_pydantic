from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import CONF_COMMAND_TOPIC, CONF_NAME, CONF_PAYLOAD_ON, CONF_RETAIN, DEFAULT_RETAIN
from .common import MqttBase, MqttEntityCommon


class Scene(MqttEntityCommon, MqttBase):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    command_topic: Annotated[str, Field(alias=CONF_COMMAND_TOPIC, min_length=1)]
    payload_on: Annotated[str | None, Field(alias=CONF_PAYLOAD_ON)] = None
    retain: Annotated[bool, Field(alias=CONF_RETAIN)] = DEFAULT_RETAIN
