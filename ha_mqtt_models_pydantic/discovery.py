from __future__ import annotations

from typing import Any, cast

from pydantic import BaseModel, ConfigDict, model_validator

from .abbreviations import ABBREVIATIONS, DEVICE_ABBREVIATIONS, ORIGIN_ABBREVIATIONS
from .components.alarm_control_panel import AlarmControlPanel
from .components.binary_sensor import BinarySensor
from .components.button import Button
from .components.camera import Camera
from .components.climate import Climate
from .components.common import DeviceDiscoveryPayload
from .components.cover import Cover
from .components.device_automation import DeviceAutomation
from .components.device_tracker import DeviceTracker
from .components.event import Event
from .components.fan import Fan
from .components.humidifier import Humidifier
from .components.image import Image
from .components.lawn_mower import LawnMower
from .components.light import LightBasic, LightJson, LightTemplate
from .components.lock import Lock
from .components.notify import Notify
from .components.number import Number
from .components.scene import Scene
from .components.select import Select
from .components.sensor import Sensor
from .components.siren import Siren
from .components.switch import Switch
from .components.tag import Tag
from .components.text import Text
from .components.update import Update
from .components.vacuum import Vacuum
from .components.valve import Valve
from .components.water_heater import WaterHeater
from .const import CONF_DEVICE, CONF_ORIGIN, CONF_SCHEMA


def expand_abbreviations(data: Any, abbreviations: dict[str, str] | None = None) -> Any:
    abbreviations = ABBREVIATIONS if abbreviations is None else abbreviations
    if not isinstance(data, dict):
        return data

    expanded: dict[str, Any] = {}
    for key, value in data.items():
        if not isinstance(key, str):
            expanded[key] = value
            continue

        new_key = abbreviations.get(key, key)
        if isinstance(value, dict):
            if new_key == CONF_DEVICE:
                expanded[new_key] = expand_abbreviations(value, DEVICE_ABBREVIATIONS)
            elif new_key == CONF_ORIGIN:
                expanded[new_key] = expand_abbreviations(value, ORIGIN_ABBREVIATIONS)
            else:
                expanded[new_key] = expand_abbreviations(value, abbreviations)
        elif isinstance(value, list):
            expanded[new_key] = [
                expand_abbreviations(item, abbreviations) if isinstance(item, dict) else item for item in value
            ]
        else:
            expanded[new_key] = value
    return expanded


COMPONENT_MODELS = {
    "alarm_control_panel": AlarmControlPanel,
    "binary_sensor": BinarySensor,
    "button": Button,
    "camera": Camera,
    "climate": Climate,
    "cover": Cover,
    "device_automation": DeviceAutomation,
    "device_tracker": DeviceTracker,
    "event": Event,
    "fan": Fan,
    "humidifier": Humidifier,
    "image": Image,
    "lawn_mower": LawnMower,
    "light": LightBasic,
    "lock": Lock,
    "notify": Notify,
    "number": Number,
    "scene": Scene,
    "select": Select,
    "sensor": Sensor,
    "siren": Siren,
    "switch": Switch,
    "tag": Tag,
    "text": Text,
    "update": Update,
    "vacuum": Vacuum,
    "valve": Valve,
    "water_heater": WaterHeater,
}


def parse_light_payload(
    payload: dict[str, Any],
    *,
    expand_aliases: bool = True,
) -> LightBasic | LightJson | LightTemplate:
    parsed = expand_abbreviations(payload) if expand_aliases else payload
    schema = parsed.get(CONF_SCHEMA, "basic")
    if schema == "basic":
        return LightBasic.model_validate(parsed)
    if schema == "json":
        return LightJson.model_validate(parsed)
    if schema == "template":
        return LightTemplate.model_validate(parsed)
    raise ValueError(f"unsupported light schema: {schema}")


def parse_component_payload(component: str, payload: dict[str, Any], *, expand_aliases: bool = True) -> BaseModel:
    if component == "light":
        return parse_light_payload(payload, expand_aliases=expand_aliases)
    parsed = expand_abbreviations(payload) if expand_aliases else payload
    try:
        model = COMPONENT_MODELS[component]
    except KeyError as err:
        raise ValueError(f"unsupported component: {component}") from err
    return cast(BaseModel, cast(Any, model).model_validate(parsed))


def parse_device_discovery_payload(payload: dict[str, Any], *, expand_aliases: bool = True) -> DeviceDiscoveryPayload:
    parsed = expand_abbreviations(payload) if expand_aliases else payload
    return DeviceDiscoveryPayload.model_validate(parsed)


class DiscoveryPayload(BaseModel):
    model_config = ConfigDict(extra="ignore")

    @model_validator(mode="before")
    @classmethod
    def expand(cls, data: Any) -> Any:
        if isinstance(data, dict):
            return expand_abbreviations(data)
        return data
