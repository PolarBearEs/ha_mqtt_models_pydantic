from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC, CONF_NAME, CONF_VALUE_TEMPLATE
from ._topics import PublishTopic
from .common import MqttEntityCommon, MqttReadWrite, NotNull


class Date(MqttEntityCommon, MqttReadWrite):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    command_template: Annotated[str | None, NotNull, Field(alias=CONF_COMMAND_TEMPLATE)] = None
    command_topic: Annotated[PublishTopic, Field(alias=CONF_COMMAND_TOPIC)]
    value_template: Annotated[str | None, NotNull, Field(alias=CONF_VALUE_TEMPLATE)] = None
