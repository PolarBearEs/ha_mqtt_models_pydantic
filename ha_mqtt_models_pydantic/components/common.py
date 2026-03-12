from __future__ import annotations

from enum import StrEnum
from typing import Annotated, Any

from pydantic import (
    AnyUrl,
    BaseModel,
    ConfigDict,
    Field,
    UrlConstraints,
    field_validator,
    model_validator,
)

from ..const import (
    AVAILABILITY_MODES,
    CONF_AVAILABILITY,
    CONF_AVAILABILITY_MODE,
    CONF_AVAILABILITY_TEMPLATE,
    CONF_AVAILABILITY_TOPIC,
    CONF_COMMAND_TOPIC,
    CONF_COMPONENTS,
    CONF_CONFIGURATION_URL,
    CONF_CONNECTIONS,
    CONF_DEFAULT_ENTITY_ID,
    CONF_DEVICE,
    CONF_ENABLED_BY_DEFAULT,
    CONF_ENCODING,
    CONF_ENTITY_CATEGORY,
    CONF_ENTITY_PICTURE,
    CONF_GROUP,
    CONF_HW_VERSION,
    CONF_ICON,
    CONF_IDENTIFIERS,
    CONF_JSON_ATTRS_TEMPLATE,
    CONF_JSON_ATTRS_TOPIC,
    CONF_MANUFACTURER,
    CONF_MODEL,
    CONF_MODEL_ID,
    CONF_NAME,
    CONF_ORIGIN,
    CONF_PAYLOAD_AVAILABLE,
    CONF_PAYLOAD_NOT_AVAILABLE,
    CONF_PLATFORM,
    CONF_QOS,
    CONF_SERIAL_NUMBER,
    CONF_STATE_TOPIC,
    CONF_SUGGESTED_AREA,
    CONF_SUPPORT_URL,
    CONF_SW_VERSION,
    CONF_TOPIC,
    CONF_UNIQUE_ID,
    CONF_VALUE_TEMPLATE,
    CONF_VIA_DEVICE,
    DEFAULT_ENCODING,
    DEFAULT_PAYLOAD_AVAILABLE,
    DEFAULT_PAYLOAD_NOT_AVAILABLE,
    DEFAULT_QOS,
)
from ._coercion import coerce_string_like_fields

PreservedUrl = Annotated[AnyUrl, UrlConstraints(preserve_empty_path=True)]


class MqttModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    @model_validator(mode="before")
    @classmethod
    def coerce_string_fields(cls, data: Any) -> Any:
        return coerce_string_like_fields(cls.model_fields, data)


class AvailabilityMode(StrEnum):
    ALL = "all"
    ANY = "any"
    LATEST = "latest"


class AvailabilityConfig(MqttModel):
    topic: Annotated[str, Field(alias=CONF_TOPIC, min_length=1)]
    payload_available: Annotated[str | None, Field(alias=CONF_PAYLOAD_AVAILABLE)] = DEFAULT_PAYLOAD_AVAILABLE
    payload_not_available: Annotated[str | None, Field(alias=CONF_PAYLOAD_NOT_AVAILABLE)] = (
        DEFAULT_PAYLOAD_NOT_AVAILABLE
    )
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None


class AvailabilityBase(MqttModel):
    availability_mode: Annotated[AvailabilityMode | None, Field(alias=CONF_AVAILABILITY_MODE)] = AvailabilityMode.LATEST
    availability_topic: Annotated[str | None, Field(alias=CONF_AVAILABILITY_TOPIC, min_length=1)] = None
    availability_template: Annotated[str | None, Field(alias=CONF_AVAILABILITY_TEMPLATE)] = None
    payload_available: Annotated[str | None, Field(alias=CONF_PAYLOAD_AVAILABLE)] = DEFAULT_PAYLOAD_AVAILABLE
    payload_not_available: Annotated[str | None, Field(alias=CONF_PAYLOAD_NOT_AVAILABLE)] = (
        DEFAULT_PAYLOAD_NOT_AVAILABLE
    )
    availability: Annotated[list[AvailabilityConfig] | None, Field(alias=CONF_AVAILABILITY)] = None

    @field_validator("availability", mode="before")
    @classmethod
    def validate_availability_list(cls, value: Any) -> Any:
        if value is None or isinstance(value, list):
            return value
        return [value]

    @field_validator("availability_mode")
    @classmethod
    def validate_availability_mode(cls, value: AvailabilityMode | None) -> AvailabilityMode | None:
        if value is None:
            return value
        if value not in AVAILABILITY_MODES:
            raise ValueError(f"availability_mode must be one of {AVAILABILITY_MODES}")
        return value

    @model_validator(mode="after")
    def validate_availability(self) -> AvailabilityBase:
        if self.availability is not None and self.availability_topic is not None:
            raise ValueError("availability and availability_topic are mutually exclusive")
        return self


class DeviceInfo(MqttModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    identifiers: Annotated[list[str] | None, Field(alias=CONF_IDENTIFIERS)] = None
    connections: Annotated[list[list[str]] | None, Field(alias=CONF_CONNECTIONS)] = None
    manufacturer: Annotated[str | None, Field(alias=CONF_MANUFACTURER)] = None
    model: Annotated[str | None, Field(alias=CONF_MODEL)] = None
    model_id: Annotated[str | None, Field(alias=CONF_MODEL_ID)] = None
    name: Annotated[str | None, Field(alias=CONF_NAME)] = None
    hw_version: Annotated[str | None, Field(alias=CONF_HW_VERSION)] = None
    serial_number: Annotated[str | None, Field(alias=CONF_SERIAL_NUMBER)] = None
    sw_version: Annotated[str | None, Field(alias=CONF_SW_VERSION)] = None
    via_device: Annotated[str | None, Field(alias=CONF_VIA_DEVICE)] = None
    suggested_area: Annotated[str | None, Field(alias=CONF_SUGGESTED_AREA)] = None
    configuration_url: Annotated[PreservedUrl | None, Field(alias=CONF_CONFIGURATION_URL)] = None

    @field_validator("identifiers", mode="before")
    @classmethod
    def validate_identifiers_list(cls, value: Any) -> list[str] | None:
        if value is None:
            return None
        if isinstance(value, list):
            return value
        return [value]

    @field_validator("connections", mode="before")
    @classmethod
    def validate_connections(cls, value: Any) -> list[list[str]] | None:
        if value is None:
            return None
        if not isinstance(value, list):
            value = [value]
        normalized: list[list[str]] = []
        for item in value:
            if not isinstance(item, (list, tuple)) or len(item) != 2:
                raise ValueError("each connection must contain exactly 2 strings")
            first, second = item
            if not isinstance(first, str) or not isinstance(second, str):
                raise ValueError("each connection value must be a string")
            normalized.append([first, second])
        return normalized

    @model_validator(mode="after")
    def validate_identifiers(self) -> DeviceInfo:
        if not self.identifiers and not self.connections:
            raise ValueError("device must define identifiers and/or connections")
        return self


class OriginInfo(MqttModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    name: Annotated[str, Field(alias=CONF_NAME, min_length=1)]
    sw_version: Annotated[str | None, Field(alias=CONF_SW_VERSION)] = None
    support_url: Annotated[PreservedUrl | None, Field(alias=CONF_SUPPORT_URL)] = None


class EntityCategory(StrEnum):
    CONFIG = "config"
    DIAGNOSTIC = "diagnostic"


class MqttBase(MqttModel):
    qos: Annotated[int | None, Field(alias=CONF_QOS, ge=0, le=2)] = DEFAULT_QOS
    encoding: Annotated[str | None, Field(alias=CONF_ENCODING)] = DEFAULT_ENCODING
    group: Annotated[list[str] | None, Field(alias=CONF_GROUP)] = None


class MqttReadOnly(MqttBase):
    state_topic: Annotated[str, Field(alias=CONF_STATE_TOPIC, min_length=1)]
    value_template: Annotated[str | None, Field(alias=CONF_VALUE_TEMPLATE)] = None


class MqttReadWrite(MqttBase):
    command_topic: Annotated[str | None, Field(alias=CONF_COMMAND_TOPIC, min_length=1)] = None
    optimistic: Annotated[bool | None, Field(alias="optimistic")] = False
    retain: Annotated[bool | None, Field(alias="retain")] = False
    state_topic: Annotated[str | None, Field(alias=CONF_STATE_TOPIC, min_length=1)] = None


class MqttEntityCommon(AvailabilityBase):
    device: Annotated[DeviceInfo | None, Field(alias=CONF_DEVICE)] = None
    entity_picture: Annotated[PreservedUrl | None, Field(alias=CONF_ENTITY_PICTURE)] = None
    origin: Annotated[OriginInfo | None, Field(alias=CONF_ORIGIN)] = None
    enabled_by_default: Annotated[bool | None, Field(alias=CONF_ENABLED_BY_DEFAULT)] = True
    entity_category: Annotated[EntityCategory | None, Field(alias=CONF_ENTITY_CATEGORY)] = None
    icon: Annotated[str | None, Field(alias=CONF_ICON)] = None
    json_attributes_topic: Annotated[str | None, Field(alias=CONF_JSON_ATTRS_TOPIC, min_length=1)] = None
    json_attributes_template: Annotated[str | None, Field(alias=CONF_JSON_ATTRS_TEMPLATE)] = None
    default_entity_id: Annotated[str | None, Field(alias=CONF_DEFAULT_ENTITY_ID)] = None
    unique_id: Annotated[str | None, Field(alias=CONF_UNIQUE_ID)] = None


class DeviceDiscoveryComponent(MqttModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    platform: Annotated[str, Field(alias=CONF_PLATFORM, min_length=1)]
    unique_id: Annotated[str | None, Field(alias=CONF_UNIQUE_ID)] = None


class DeviceDiscoveryPayload(MqttBase, AvailabilityBase):
    device: Annotated[DeviceInfo, Field(alias=CONF_DEVICE)]
    components: Annotated[dict[str, DeviceDiscoveryComponent], Field(alias=CONF_COMPONENTS)]
    origin: Annotated[OriginInfo, Field(alias=CONF_ORIGIN)]
    state_topic: Annotated[str | None, Field(alias=CONF_STATE_TOPIC, min_length=1)] = None
    command_topic: Annotated[str | None, Field(alias=CONF_COMMAND_TOPIC, min_length=1)] = None
