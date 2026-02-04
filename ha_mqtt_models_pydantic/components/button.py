from __future__ import annotations

from typing import Annotated

from pydantic import ConfigDict, Field

from ..const import (
    CONF_COMMAND_TEMPLATE,
    CONF_COMMAND_TOPIC,
    CONF_DEVICE_CLASS,
    CONF_NAME,
    CONF_PAYLOAD_PRESS,
    CONF_RETAIN,
    DEFAULT_PAYLOAD_PRESS,
    DEFAULT_RETAIN,
)
from .common import MqttBase, MqttEntityCommon


class Button(MqttEntityCommon, MqttBase):
    model_config = ConfigDict(populate_by_name=True)

    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    command_template: Annotated[str | None, Field(alias=CONF_COMMAND_TEMPLATE)] = None
    command_topic: Annotated[str, Field(alias=CONF_COMMAND_TOPIC)]
    device_class: Annotated[str | None, Field(alias=CONF_DEVICE_CLASS)] = None
    payload_press: Annotated[str | None, Field(alias=CONF_PAYLOAD_PRESS)] = DEFAULT_PAYLOAD_PRESS
    retain: Annotated[bool | None, Field(alias=CONF_RETAIN)] = DEFAULT_RETAIN
