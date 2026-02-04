from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..const import (
    CONF_CODE,
    CONF_CODE_ARM_REQUIRED,
    CONF_CODE_DISARM_REQUIRED,
    CONF_CODE_TRIGGER_REQUIRED,
    CONF_COMMAND_TEMPLATE,
    CONF_COMMAND_TOPIC,
    CONF_NAME,
    CONF_PAYLOAD_ARM_AWAY,
    CONF_PAYLOAD_ARM_CUSTOM_BYPASS,
    CONF_PAYLOAD_ARM_HOME,
    CONF_PAYLOAD_ARM_NIGHT,
    CONF_PAYLOAD_ARM_VACATION,
    CONF_PAYLOAD_DISARM,
    CONF_PAYLOAD_TRIGGER,
    CONF_STATE_TOPIC,
    CONF_SUPPORTED_FEATURES,
    CONF_VALUE_TEMPLATE,
    DEFAULT_ALARM_CONTROL_PANEL_COMMAND_TEMPLATE,
    DEFAULT_PAYLOAD_ARM_AWAY,
    DEFAULT_PAYLOAD_ARM_CUSTOM_BYPASS,
    DEFAULT_PAYLOAD_ARM_HOME,
    DEFAULT_PAYLOAD_ARM_NIGHT,
    DEFAULT_PAYLOAD_ARM_VACATION,
    DEFAULT_PAYLOAD_DISARM,
    DEFAULT_PAYLOAD_TRIGGER,
)
from .common import MqttEntityCommon, MqttReadWrite


class AlarmControlPanel(MqttEntityCommon, MqttReadWrite):
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    command_topic: Annotated[str, Field(alias=CONF_COMMAND_TOPIC, min_length=1)]
    state_topic: Annotated[str, Field(alias=CONF_STATE_TOPIC, min_length=1)]
    code: Annotated[str | None, Field(alias=CONF_CODE)] = None
    code_arm_required: Annotated[bool | None, Field(alias=CONF_CODE_ARM_REQUIRED)] = True
    code_disarm_required: Annotated[bool | None, Field(alias=CONF_CODE_DISARM_REQUIRED)] = True
    code_trigger_required: Annotated[bool | None, Field(alias=CONF_CODE_TRIGGER_REQUIRED)] = True
    command_template: Annotated[str | None, Field(alias=CONF_COMMAND_TEMPLATE)] = (
        DEFAULT_ALARM_CONTROL_PANEL_COMMAND_TEMPLATE
    )
    payload_arm_away: Annotated[str | None, Field(alias=CONF_PAYLOAD_ARM_AWAY)] = DEFAULT_PAYLOAD_ARM_AWAY
    payload_arm_home: Annotated[str | None, Field(alias=CONF_PAYLOAD_ARM_HOME)] = DEFAULT_PAYLOAD_ARM_HOME
    payload_arm_night: Annotated[str | None, Field(alias=CONF_PAYLOAD_ARM_NIGHT)] = DEFAULT_PAYLOAD_ARM_NIGHT
    payload_arm_vacation: Annotated[str | None, Field(alias=CONF_PAYLOAD_ARM_VACATION)] = DEFAULT_PAYLOAD_ARM_VACATION
    payload_arm_custom_bypass: Annotated[str | None, Field(alias=CONF_PAYLOAD_ARM_CUSTOM_BYPASS)] = (
        DEFAULT_PAYLOAD_ARM_CUSTOM_BYPASS
    )
    payload_disarm: Annotated[str | None, Field(alias=CONF_PAYLOAD_DISARM)] = DEFAULT_PAYLOAD_DISARM
    payload_trigger: Annotated[str | None, Field(alias=CONF_PAYLOAD_TRIGGER)] = DEFAULT_PAYLOAD_TRIGGER
    supported_features: Annotated[list[str] | None, Field(alias=CONF_SUPPORTED_FEATURES)] = None
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None
