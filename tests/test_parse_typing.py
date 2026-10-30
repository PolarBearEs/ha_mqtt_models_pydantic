from __future__ import annotations

import re
from typing import assert_type, get_args, get_overloads

from ha_mqtt_models_pydantic import (
    COMPONENT_MODELS,
    ComponentModel,
    ComponentName,
    DeviceAutomation,
    DeviceClassBase,
    EntityModel,
    InfraredEmitter,
    InfraredReceiver,
    LightBasic,
    LightJson,
    LightTemplate,
    MqttEntityCommon,
    Sensor,
    Switch,
    Tag,
    Vacuum,
    parse_component_payload,
)
from ha_mqtt_models_pydantic._typing import ComponentPayloadParser

# assert_type is a no-op at runtime; mypy checks these against the parse_component_payload overloads.


def test_literal_component_returns_specific_model() -> None:
    sensor = parse_component_payload("sensor", {"stat_t": "sensor/state"})
    assert_type(sensor, Sensor)
    assert isinstance(sensor, Sensor)
    assert sensor.state_topic == "sensor/state"

    switch = parse_component_payload("switch", {"cmd_t": "switch/cmd"}, expand_aliases=True)
    assert_type(switch, Switch)
    assert isinstance(switch, Switch)

    vacuum = parse_component_payload("vacuum", {"command_topic": "vacuum/cmd"}, expand_aliases=False)
    assert_type(vacuum, Vacuum)
    assert isinstance(vacuum, Vacuum)


def test_schema_dispatched_components_return_unions() -> None:
    light = parse_component_payload("light", {"schema": "json", "cmd_t": "light/cmd"})
    assert_type(light, LightBasic | LightJson | LightTemplate)
    assert isinstance(light, LightJson)

    infrared = parse_component_payload("infrared", {"schema": "receiver", "stat_t": "infrared/received"})
    assert_type(infrared, InfraredEmitter | InfraredReceiver)
    assert isinstance(infrared, InfraredReceiver)


def test_dynamic_component_returns_component_model_union() -> None:
    component: str = "sensor"
    model = parse_component_payload(component, {"stat_t": "sensor/state"})
    assert_type(model, ComponentModel)
    assert isinstance(model, Sensor)


def test_overloads_cover_every_registered_component() -> None:
    schema_dispatched = {
        "infrared": "InfraredEmitter | InfraredReceiver",
        "light": "LightBasic | LightJson | LightTemplate",
    }

    # A Protocol method without an implementation resolves to typing's overload dummy, so look the
    # overloads up by the module and qualified name they are registered under.
    def protocol_call() -> None: ...

    protocol_call.__module__ = ComponentPayloadParser.__module__
    protocol_call.__qualname__ = f"{ComponentPayloadParser.__qualname__}.__call__"

    returns: dict[str, str] = {}
    for overload_ in get_overloads(protocol_call):
        if match := re.fullmatch(r"Literal\[['\"](\w+)['\"]\]", overload_.__annotations__["component"]):
            returns[match.group(1)] = overload_.__annotations__["return"]

    expected = {name: schema_dispatched.get(name, model.__name__) for name, model in COMPONENT_MODELS.items()}
    assert returns == expected


def test_type_aliases_match_registered_components() -> None:
    assert set(get_args(ComponentName)) == set(COMPONENT_MODELS)

    models = set(get_args(ComponentModel))
    assert set(COMPONENT_MODELS.values()) <= models
    assert models - set(COMPONENT_MODELS.values()) == {InfraredReceiver, LightJson, LightTemplate}

    entities = set(get_args(EntityModel))
    assert entities == models - {DeviceAutomation, Tag}
    assert all(issubclass(model, MqttEntityCommon) for model in entities)
    assert not any(issubclass(model, MqttEntityCommon) for model in models - entities)


def test_shared_fields_live_on_base_classes() -> None:
    entity: EntityModel = parse_component_payload("sensor", {"name": "Temp", "dev_cla": "temperature", "stat_t": "t"})
    assert entity.name == "Temp"
    assert isinstance(entity, DeviceClassBase)
    assert entity.device_class == "temperature"

    humidifier = parse_component_payload("humidifier", {"cmd_t": "h/cmd", "target_humidity_command_topic": "h/t"})
    assert isinstance(humidifier, DeviceClassBase)
    assert humidifier.device_class == "humidifier"
