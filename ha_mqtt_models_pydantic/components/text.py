from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import CONF_COMMAND_TEMPLATE, CONF_MAX, CONF_MIN, CONF_MODE, CONF_NAME, CONF_PATTERN, CONF_VALUE_TEMPLATE
from .common import MqttEntityCommon, MqttReadWrite


class Text(MqttEntityCommon, MqttReadWrite):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    command_template: Annotated[str | None, Field(alias=CONF_COMMAND_TEMPLATE)] = None
    max: Annotated[int | None, Field(alias=CONF_MAX)] = None
    min: Annotated[int | None, Field(alias=CONF_MIN)] = None
    mode: Annotated[str, Field(alias=CONF_MODE)] = "text"
    pattern: Annotated[str | None, Field(alias=CONF_PATTERN)] = None
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None
