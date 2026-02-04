from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import (
    CONF_CODE_FORMAT,
    CONF_COMMAND_TEMPLATE,
    CONF_NAME,
    CONF_PAYLOAD_LOCK,
    CONF_PAYLOAD_OPEN,
    CONF_PAYLOAD_RESET,
    CONF_PAYLOAD_UNLOCK,
    CONF_STATE_JAMMED,
    CONF_STATE_LOCKED,
    CONF_STATE_LOCKING,
    CONF_STATE_OPEN,
    CONF_STATE_OPENING,
    CONF_STATE_UNLOCKED,
    CONF_STATE_UNLOCKING,
    CONF_VALUE_TEMPLATE,
    DEFAULT_PAYLOAD_LOCK,
    DEFAULT_PAYLOAD_OPEN,
    DEFAULT_PAYLOAD_RESET,
    DEFAULT_PAYLOAD_UNLOCK,
    DEFAULT_STATE_JAMMED,
    DEFAULT_STATE_LOCKED,
    DEFAULT_STATE_LOCKING,
    DEFAULT_STATE_OPEN,
    DEFAULT_STATE_OPENING,
    DEFAULT_STATE_UNLOCKED,
    DEFAULT_STATE_UNLOCKING,
)
from .common import MqttEntityCommon, MqttReadWrite


class Lock(MqttEntityCommon, MqttReadWrite):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    code_format: Annotated[str | None, Field(alias=CONF_CODE_FORMAT)] = None
    command_template: Annotated[str | None, Field(alias=CONF_COMMAND_TEMPLATE)] = None
    payload_lock: Annotated[str | None, Field(alias=CONF_PAYLOAD_LOCK)] = DEFAULT_PAYLOAD_LOCK
    payload_open: Annotated[str | None, Field(alias=CONF_PAYLOAD_OPEN)] = DEFAULT_PAYLOAD_OPEN
    payload_reset: Annotated[str | None, Field(alias=CONF_PAYLOAD_RESET)] = DEFAULT_PAYLOAD_RESET
    payload_unlock: Annotated[str | None, Field(alias=CONF_PAYLOAD_UNLOCK)] = DEFAULT_PAYLOAD_UNLOCK
    state_jammed: Annotated[str | None, Field(alias=CONF_STATE_JAMMED)] = DEFAULT_STATE_JAMMED
    state_locked: Annotated[str | None, Field(alias=CONF_STATE_LOCKED)] = DEFAULT_STATE_LOCKED
    state_locking: Annotated[str | None, Field(alias=CONF_STATE_LOCKING)] = DEFAULT_STATE_LOCKING
    state_open: Annotated[str | None, Field(alias=CONF_STATE_OPEN)] = DEFAULT_STATE_OPEN
    state_opening: Annotated[str | None, Field(alias=CONF_STATE_OPENING)] = DEFAULT_STATE_OPENING
    state_unlocked: Annotated[str | None, Field(alias=CONF_STATE_UNLOCKED)] = DEFAULT_STATE_UNLOCKED
    state_unlocking: Annotated[str | None, Field(alias=CONF_STATE_UNLOCKING)] = DEFAULT_STATE_UNLOCKING
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None
