from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC, CONF_NAME, CONF_RETAIN, DEFAULT_RETAIN
from .common import MqttBase, MqttEntityCommon


class Notify(MqttEntityCommon, MqttBase):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    command_template: Annotated[str | None, Field(alias=CONF_COMMAND_TEMPLATE)] = None
    command_topic: Annotated[str, Field(alias=CONF_COMMAND_TOPIC, min_length=1)]
    retain: Annotated[bool | None, Field(alias=CONF_RETAIN)] = DEFAULT_RETAIN
