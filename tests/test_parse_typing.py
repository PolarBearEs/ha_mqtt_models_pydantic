from __future__ import annotations

from typing import assert_type

from ha_mqtt_models_pydantic import (
    ComponentModel,
    InfraredEmitter,
    InfraredReceiver,
    LightBasic,
    LightJson,
    LightTemplate,
    Sensor,
    Switch,
    Vacuum,
    parse_component_payload,
)

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
