from __future__ import annotations

from typing import Annotated

from pydantic import Field, model_validator

from ..const import (
    CONF_CONTENT_TYPE,
    CONF_IMAGE_ENCODING,
    CONF_IMAGE_TOPIC,
    CONF_NAME,
    CONF_URL_TEMPLATE,
    CONF_URL_TOPIC,
)
from .common import MqttBase, MqttEntityCommon


class Image(MqttEntityCommon, MqttBase):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    content_type: Annotated[str | None, Field(alias=CONF_CONTENT_TYPE)] = None
    image_topic: Annotated[str | None, Field(alias=CONF_IMAGE_TOPIC, min_length=1)] = None
    image_encoding: Annotated[str | None, Field(alias=CONF_IMAGE_ENCODING)] = None
    url_template: Annotated[str | None, Field(alias=CONF_URL_TEMPLATE)] = None
    url_topic: Annotated[str | None, Field(alias=CONF_URL_TOPIC, min_length=1)] = None

    @model_validator(mode="after")
    def validate_topics(self) -> Image:
        if self.image_topic is None and self.url_topic is None:
            raise ValueError("Expected one of [`image_topic`, `url_topic`], got none")
        if self.content_type is not None and self.url_topic is not None:
            raise ValueError("Option `content_type` can not be used together with `url_topic`")
        return self
