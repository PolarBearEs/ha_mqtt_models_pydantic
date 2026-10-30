from __future__ import annotations

from typing import Annotated

from pydantic import ConfigDict, Field

from ..const import (
    CONF_COMMAND_TEMPLATE,
    CONF_NAME,
    CONF_OPTIONS,
    CONF_VALUE_TEMPLATE,
)
from .common import MqttEntityCommon, MqttReadWrite


class Select(MqttEntityCommon, MqttReadWrite):
    model_config = ConfigDict(populate_by_name=True)

    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    command_template: Annotated[str | None, Field(alias=CONF_COMMAND_TEMPLATE)] = None
    options: Annotated[list[str], Field(alias=CONF_OPTIONS)]
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None
