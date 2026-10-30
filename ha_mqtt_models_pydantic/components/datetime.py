from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC, CONF_TIMEZONE, CONF_VALUE_TEMPLATE
from ._topics import PublishTopic
from .common import MqttEntityCommon, MqttReadWrite, NotNull


class DateTime(MqttEntityCommon, MqttReadWrite):
    command_template: Annotated[str | None, NotNull, Field(alias=CONF_COMMAND_TEMPLATE)] = None
    command_topic: Annotated[PublishTopic, Field(alias=CONF_COMMAND_TOPIC)]
    timezone: Annotated[str | None, NotNull, Field(alias=CONF_TIMEZONE)] = None
    value_template: Annotated[str | None, NotNull, Field(alias=CONF_VALUE_TEMPLATE)] = None
