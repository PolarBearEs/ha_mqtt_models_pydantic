from __future__ import annotations

from typing import Any, Literal, TypeAlias, overload

from pydantic import BaseModel, ConfigDict, model_validator

from .abbreviations import ABBREVIATIONS, DEVICE_ABBREVIATIONS, ORIGIN_ABBREVIATIONS
from .components.alarm_control_panel import AlarmControlPanel
from .components.binary_sensor import BinarySensor
from .components.button import Button
from .components.camera import Camera
from .components.climate import Climate
from .components.common import DeviceDiscoveryPayload
from .components.cover import Cover
from .components.date import Date
from .components.datetime import DateTime
from .components.device_automation import DeviceAutomation
from .components.device_tracker import DeviceTracker
from .components.event import Event
from .components.fan import Fan
from .components.humidifier import Humidifier
from .components.image import Image
from .components.infrared import InfraredEmitter, InfraredReceiver
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
from .components.time import Time
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


ComponentModel: TypeAlias = (
    AlarmControlPanel
    | BinarySensor
    | Button
    | Camera
    | Climate
    | Cover
    | Date
    | DateTime
    | DeviceAutomation
    | DeviceTracker
    | Event
    | Fan
    | Humidifier
    | Image
    | InfraredEmitter
    | InfraredReceiver
    | LawnMower
    | LightBasic
    | LightJson
    | LightTemplate
    | Lock
    | Notify
    | Number
    | Scene
    | Select
    | Sensor
    | Siren
    | Switch
    | Tag
    | Text
    | Time
    | Update
    | Vacuum
    | Valve
    | WaterHeater
)


COMPONENT_MODELS: dict[str, type[ComponentModel]] = {
    "alarm_control_panel": AlarmControlPanel,
    "binary_sensor": BinarySensor,
    "button": Button,
    "camera": Camera,
    "climate": Climate,
    "cover": Cover,
    "date": Date,
    "datetime": DateTime,
    "device_automation": DeviceAutomation,
    "device_tracker": DeviceTracker,
    "event": Event,
    "fan": Fan,
    "humidifier": Humidifier,
    "image": Image,
    # Infrared payloads are dispatched on their required schema by parse_infrared_payload
    "infrared": InfraredEmitter,
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
    "time": Time,
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


def parse_infrared_payload(
    payload: dict[str, Any],
    *,
    expand_aliases: bool = True,
) -> InfraredEmitter | InfraredReceiver:
    parsed = expand_abbreviations(payload) if expand_aliases else payload
    schema = parsed.get(CONF_SCHEMA)
    if schema == "emitter":
        return InfraredEmitter.model_validate(parsed)
    if schema == "receiver":
        return InfraredReceiver.model_validate(parsed)
    raise ValueError(f"unsupported infrared schema: {schema}")


@overload
def parse_component_payload(
    component: Literal["alarm_control_panel"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> AlarmControlPanel: ...


@overload
def parse_component_payload(
    component: Literal["binary_sensor"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> BinarySensor: ...


@overload
def parse_component_payload(
    component: Literal["button"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Button: ...


@overload
def parse_component_payload(
    component: Literal["camera"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Camera: ...


@overload
def parse_component_payload(
    component: Literal["climate"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Climate: ...


@overload
def parse_component_payload(
    component: Literal["cover"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Cover: ...


@overload
def parse_component_payload(
    component: Literal["date"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Date: ...


@overload
def parse_component_payload(
    component: Literal["datetime"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> DateTime: ...


@overload
def parse_component_payload(
    component: Literal["device_automation"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> DeviceAutomation: ...


@overload
def parse_component_payload(
    component: Literal["device_tracker"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> DeviceTracker: ...


@overload
def parse_component_payload(
    component: Literal["event"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Event: ...


@overload
def parse_component_payload(
    component: Literal["fan"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Fan: ...


@overload
def parse_component_payload(
    component: Literal["humidifier"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Humidifier: ...


@overload
def parse_component_payload(
    component: Literal["image"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Image: ...


@overload
def parse_component_payload(
    component: Literal["infrared"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> InfraredEmitter | InfraredReceiver: ...


@overload
def parse_component_payload(
    component: Literal["lawn_mower"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> LawnMower: ...


@overload
def parse_component_payload(
    component: Literal["light"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> LightBasic | LightJson | LightTemplate: ...


@overload
def parse_component_payload(
    component: Literal["lock"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Lock: ...


@overload
def parse_component_payload(
    component: Literal["notify"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Notify: ...


@overload
def parse_component_payload(
    component: Literal["number"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Number: ...


@overload
def parse_component_payload(
    component: Literal["scene"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Scene: ...


@overload
def parse_component_payload(
    component: Literal["select"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Select: ...


@overload
def parse_component_payload(
    component: Literal["sensor"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Sensor: ...


@overload
def parse_component_payload(
    component: Literal["siren"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Siren: ...


@overload
def parse_component_payload(
    component: Literal["switch"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Switch: ...


@overload
def parse_component_payload(
    component: Literal["tag"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Tag: ...


@overload
def parse_component_payload(
    component: Literal["text"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Text: ...


@overload
def parse_component_payload(
    component: Literal["time"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Time: ...


@overload
def parse_component_payload(
    component: Literal["update"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Update: ...


@overload
def parse_component_payload(
    component: Literal["vacuum"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Vacuum: ...


@overload
def parse_component_payload(
    component: Literal["valve"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> Valve: ...


@overload
def parse_component_payload(
    component: Literal["water_heater"], payload: dict[str, Any], *, expand_aliases: bool = ...
) -> WaterHeater: ...


@overload
def parse_component_payload(
    component: str, payload: dict[str, Any], *, expand_aliases: bool = ...
) -> ComponentModel: ...


def parse_component_payload(component: str, payload: dict[str, Any], *, expand_aliases: bool = True) -> ComponentModel:
    if component == "light":
        return parse_light_payload(payload, expand_aliases=expand_aliases)
    if component == "infrared":
        return parse_infrared_payload(payload, expand_aliases=expand_aliases)
    parsed = expand_abbreviations(payload) if expand_aliases else payload
    try:
        model = COMPONENT_MODELS[component]
    except KeyError as err:
        raise ValueError(f"unsupported component: {component}") from err
    return model.model_validate(parsed)


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
