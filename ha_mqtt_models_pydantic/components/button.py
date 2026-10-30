from __future__ import annotations

from typing import Annotated

from pydantic import ConfigDict, Field

from ..const import (
    CONF_COMMAND_TEMPLATE,
    CONF_COMMAND_TOPIC,
    CONF_PAYLOAD_PRESS,
    CONF_RETAIN,
    DEFAULT_PAYLOAD_PRESS,
    DEFAULT_RETAIN,
)
from .common import DeviceClassBase, MqttBase, MqttEntityCommon


class Button(MqttEntityCommon, DeviceClassBase, MqttBase):
    model_config = ConfigDict(populate_by_name=True)

    command_template: Annotated[str | None, Field(alias=CONF_COMMAND_TEMPLATE)] = None
    command_topic: Annotated[str, Field(alias=CONF_COMMAND_TOPIC)]
    payload_press: Annotated[str, Field(alias=CONF_PAYLOAD_PRESS)] = DEFAULT_PAYLOAD_PRESS
    retain: Annotated[bool, Field(alias=CONF_RETAIN)] = DEFAULT_RETAIN
