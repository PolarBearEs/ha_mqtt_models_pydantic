from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import CONF_IMAGE_ENCODING, CONF_NAME, CONF_TOPIC
from .common import MqttBase, MqttEntityCommon


class Camera(MqttEntityCommon, MqttBase):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    topic: Annotated[str, Field(alias=CONF_TOPIC, min_length=1)]
    image_encoding: Annotated[str | None, Field(alias=CONF_IMAGE_ENCODING)] = None
