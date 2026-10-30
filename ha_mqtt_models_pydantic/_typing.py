"""Static typing for parse_component_payload, kept apart from the parsing logic."""

from __future__ import annotations

from typing import Any, Literal, Protocol, TypeAlias, overload

from .components import (
    AlarmControlPanel,
    BinarySensor,
    Button,
    Camera,
    Climate,
    Cover,
    Date,
    DateTime,
    DeviceAutomation,
    DeviceTracker,
    Event,
    Fan,
    Humidifier,
    Image,
    InfraredEmitter,
    InfraredReceiver,
    LawnMower,
    LightBasic,
    LightJson,
    LightTemplate,
    Lock,
    Notify,
    Number,
    Scene,
    Select,
    Sensor,
    Siren,
    Switch,
    Tag,
    Text,
    Time,
    Update,
    Vacuum,
    Valve,
    WaterHeater,
)

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

Payload: TypeAlias = dict[str, Any]


class ComponentPayloadParser(Protocol):
    """Map each literal component name to the model parse_component_payload returns."""

    @overload
    def __call__(
        self, component: Literal["alarm_control_panel"], payload: Payload, *, expand_aliases: bool = ...
    ) -> AlarmControlPanel: ...
    @overload
    def __call__(
        self, component: Literal["binary_sensor"], payload: Payload, *, expand_aliases: bool = ...
    ) -> BinarySensor: ...
    @overload
    def __call__(self, component: Literal["button"], payload: Payload, *, expand_aliases: bool = ...) -> Button: ...
    @overload
    def __call__(self, component: Literal["camera"], payload: Payload, *, expand_aliases: bool = ...) -> Camera: ...
    @overload
    def __call__(self, component: Literal["climate"], payload: Payload, *, expand_aliases: bool = ...) -> Climate: ...
    @overload
    def __call__(self, component: Literal["cover"], payload: Payload, *, expand_aliases: bool = ...) -> Cover: ...
    @overload
    def __call__(self, component: Literal["date"], payload: Payload, *, expand_aliases: bool = ...) -> Date: ...
    @overload
    def __call__(self, component: Literal["datetime"], payload: Payload, *, expand_aliases: bool = ...) -> DateTime: ...
    @overload
    def __call__(
        self, component: Literal["device_automation"], payload: Payload, *, expand_aliases: bool = ...
    ) -> DeviceAutomation: ...
    @overload
    def __call__(
        self, component: Literal["device_tracker"], payload: Payload, *, expand_aliases: bool = ...
    ) -> DeviceTracker: ...
    @overload
    def __call__(self, component: Literal["event"], payload: Payload, *, expand_aliases: bool = ...) -> Event: ...
    @overload
    def __call__(self, component: Literal["fan"], payload: Payload, *, expand_aliases: bool = ...) -> Fan: ...
    @overload
    def __call__(
        self, component: Literal["humidifier"], payload: Payload, *, expand_aliases: bool = ...
    ) -> Humidifier: ...
    @overload
    def __call__(self, component: Literal["image"], payload: Payload, *, expand_aliases: bool = ...) -> Image: ...
    @overload
    def __call__(
        self, component: Literal["infrared"], payload: Payload, *, expand_aliases: bool = ...
    ) -> InfraredEmitter | InfraredReceiver: ...
    @overload
    def __call__(
        self, component: Literal["lawn_mower"], payload: Payload, *, expand_aliases: bool = ...
    ) -> LawnMower: ...
    @overload
    def __call__(
        self, component: Literal["light"], payload: Payload, *, expand_aliases: bool = ...
    ) -> LightBasic | LightJson | LightTemplate: ...
    @overload
    def __call__(self, component: Literal["lock"], payload: Payload, *, expand_aliases: bool = ...) -> Lock: ...
    @overload
    def __call__(self, component: Literal["notify"], payload: Payload, *, expand_aliases: bool = ...) -> Notify: ...
    @overload
    def __call__(self, component: Literal["number"], payload: Payload, *, expand_aliases: bool = ...) -> Number: ...
    @overload
    def __call__(self, component: Literal["scene"], payload: Payload, *, expand_aliases: bool = ...) -> Scene: ...
    @overload
    def __call__(self, component: Literal["select"], payload: Payload, *, expand_aliases: bool = ...) -> Select: ...
    @overload
    def __call__(self, component: Literal["sensor"], payload: Payload, *, expand_aliases: bool = ...) -> Sensor: ...
    @overload
    def __call__(self, component: Literal["siren"], payload: Payload, *, expand_aliases: bool = ...) -> Siren: ...
    @overload
    def __call__(self, component: Literal["switch"], payload: Payload, *, expand_aliases: bool = ...) -> Switch: ...
    @overload
    def __call__(self, component: Literal["tag"], payload: Payload, *, expand_aliases: bool = ...) -> Tag: ...
    @overload
    def __call__(self, component: Literal["text"], payload: Payload, *, expand_aliases: bool = ...) -> Text: ...
    @overload
    def __call__(self, component: Literal["time"], payload: Payload, *, expand_aliases: bool = ...) -> Time: ...
    @overload
    def __call__(self, component: Literal["update"], payload: Payload, *, expand_aliases: bool = ...) -> Update: ...
    @overload
    def __call__(self, component: Literal["vacuum"], payload: Payload, *, expand_aliases: bool = ...) -> Vacuum: ...
    @overload
    def __call__(self, component: Literal["valve"], payload: Payload, *, expand_aliases: bool = ...) -> Valve: ...
    @overload
    def __call__(
        self, component: Literal["water_heater"], payload: Payload, *, expand_aliases: bool = ...
    ) -> WaterHeater: ...
    @overload
    def __call__(self, component: str, payload: Payload, *, expand_aliases: bool = ...) -> ComponentModel: ...
