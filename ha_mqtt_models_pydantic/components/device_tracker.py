from __future__ import annotations

from typing import Annotated

from pydantic import Field, model_validator

from ..const import (
    CONF_NAME,
    CONF_PAYLOAD_HOME,
    CONF_PAYLOAD_NOT_HOME,
    CONF_PAYLOAD_RESET,
    CONF_SOURCE_TYPE,
    CONF_STATE_TOPIC,
    CONF_VALUE_TEMPLATE,
    DEFAULT_PAYLOAD_HOME,
    DEFAULT_PAYLOAD_NOT_HOME,
    DEFAULT_PAYLOAD_RESET,
)
from .common import MqttBase, MqttEntityCommon


class DeviceTracker(MqttEntityCommon, MqttBase):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    state_topic: Annotated[str | None, Field(alias=CONF_STATE_TOPIC, min_length=1)] = None
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None
    payload_home: Annotated[str | None, Field(alias=CONF_PAYLOAD_HOME)] = DEFAULT_PAYLOAD_HOME
    payload_not_home: Annotated[str | None, Field(alias=CONF_PAYLOAD_NOT_HOME)] = DEFAULT_PAYLOAD_NOT_HOME
    payload_reset: Annotated[str | None, Field(alias=CONF_PAYLOAD_RESET)] = DEFAULT_PAYLOAD_RESET
    source_type: Annotated[str | None, Field(alias=CONF_SOURCE_TYPE)] = "gps"

    @model_validator(mode="after")
    def validate_topics(self) -> DeviceTracker:
        if self.state_topic is None and self.json_attributes_topic is None:
            raise ValueError("device_tracker requires state_topic or json_attributes_topic")
        return self
