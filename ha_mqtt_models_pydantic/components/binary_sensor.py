from __future__ import annotations

from typing import Annotated

from pydantic import ConfigDict, Field

from ..const import (
    CONF_DEVICE_CLASS,
    CONF_EXPIRE_AFTER,
    CONF_FORCE_UPDATE,
    CONF_NAME,
    CONF_OFF_DELAY,
    CONF_PAYLOAD_OFF,
    CONF_PAYLOAD_ON,
    DEFAULT_PAYLOAD_OFF,
    DEFAULT_PAYLOAD_ON,
)
from .common import MqttEntityCommon, MqttReadOnly


class BinarySensor(MqttEntityCommon, MqttReadOnly):
    model_config = ConfigDict(populate_by_name=True)

    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    device_class: Annotated[str | None, Field(alias=CONF_DEVICE_CLASS)] = None
    expire_after: Annotated[int | None, Field(gt=0, alias=CONF_EXPIRE_AFTER)] = None
    force_update: Annotated[bool, Field(alias=CONF_FORCE_UPDATE)] = False
    off_delay: Annotated[int | None, Field(gt=0, alias=CONF_OFF_DELAY)] = None
    payload_off: Annotated[str, Field(alias=CONF_PAYLOAD_OFF)] = DEFAULT_PAYLOAD_OFF
    payload_on: Annotated[str, Field(alias=CONF_PAYLOAD_ON)] = DEFAULT_PAYLOAD_ON
