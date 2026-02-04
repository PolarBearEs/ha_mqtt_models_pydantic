from __future__ import annotations

from typing import Any

import pytest
from pydantic import ValidationError

from ha_mqtt_models_pydantic.components.light import LightBasic, LightJson, LightTemplate
from ha_mqtt_models_pydantic.discovery import (
    COMPONENT_MODELS,
    parse_component_payload,
    parse_device_discovery_payload,
    parse_light_payload,
)

ENTITY_COMMON: dict[str, Any] = {
    "name": "Demo Entity",
    "uniq_id": "demo-uid",
    "def_ent_id": "sensor.demo_entity",
    "dev": {
        "ids": ["device-1"],
        "name": "Demo Device",
        "mf": "ACME",
    },
    "avty_t": "availability/topic",
}

MINIMAL_COMPONENT_PAYLOADS: dict[str, dict[str, Any]] = {
    "alarm_control_panel": {"cmd_t": "alarm/set", "stat_t": "alarm/state"},
    "binary_sensor": {"stat_t": "binary_sensor/state"},
    "button": {"cmd_t": "button/press"},
    "camera": {"t": "camera/image"},
    "climate": {"mode_cmd_t": "climate/mode/set"},
    "cover": {"cmd_t": "cover/cmd"},
    "device_automation": {
        "atype": "trigger",
        "dev": {"ids": ["device-1"]},
        "stype": "button_1",
        "t": "trigger/topic",
        "type": "button_short_press",
    },
    "device_tracker": {"stat_t": "tracker/state"},
    "event": {"stat_t": "event/state", "evt_typ": ["pressed"]},
    "fan": {"cmd_t": "fan/cmd"},
    "humidifier": {"hum_cmd_t": "humidifier/humidity/set"},
    "image": {"img_t": "image/topic"},
    "lawn_mower": {"dock_cmd_t": "mower/dock"},
    "lock": {"cmd_t": "lock/cmd"},
    "notify": {"cmd_t": "notify/send"},
    "number": {"cmd_t": "number/set"},
    "scene": {"cmd_t": "scene/activate"},
    "select": {"ops": ["one", "two"]},
    "sensor": {"stat_t": "sensor/state"},
    "siren": {"cmd_t": "siren/cmd"},
    "switch": {"cmd_t": "switch/cmd"},
    "tag": {"t": "tag/topic"},
    "text": {"cmd_t": "text/set"},
    "update": {"stat_t": "update/state"},
    "vacuum": {"cmd_t": "vacuum/cmd"},
    "valve": {"cmd_t": "valve/cmd"},
    "water_heater": {"mode_cmd_t": "water_heater/mode/set"},
}

FULL_COMPONENT_PAYLOADS: dict[str, dict[str, Any]] = {
    "alarm_control_panel": {
        **ENTITY_COMMON,
        "cmd_t": "alarm/set",
        "stat_t": "alarm/state",
        "pl_arm_away": "AWAY",
        "pl_disarm": "DISARM",
        "sup_feat": ["arm_home"],
    },
    "binary_sensor": {
        **ENTITY_COMMON,
        "stat_t": "binary_sensor/state",
        "dev_cla": "motion",
        "exp_aft": 30,
        "frc_upd": True,
    },
    "button": {
        **ENTITY_COMMON,
        "cmd_t": "button/press",
        "pl_prs": "PRESS",
        "ret": True,
    },
    "camera": {
        **ENTITY_COMMON,
        "t": "camera/image",
        "img_e": "b64",
    },
    "climate": {
        **ENTITY_COMMON,
        "mode_cmd_t": "climate/mode/set",
        "mode_stat_t": "climate/mode/state",
        "temp_cmd_t": "climate/temp/set",
        "temp_stat_t": "climate/temp/state",
        "curr_temp_t": "climate/temp/current",
        "hum_cmd_t": "climate/humidity/set",
        "hum_stat_t": "climate/humidity/state",
        "min_hum": 35,
        "max_hum": 90,
        "pr_modes": ["eco", "boost"],
        "pr_mode_cmd_t": "climate/preset/set",
    },
    "cover": {
        **ENTITY_COMMON,
        "cmd_t": "cover/cmd",
        "stat_t": "cover/state",
        "pos_t": "cover/position/state",
        "set_pos_t": "cover/position/set",
        "tilt_status_t": "cover/tilt/state",
        "tilt_cmd_t": "cover/tilt/set",
    },
    "device_automation": {
        "atype": "trigger",
        "dev": {"ids": ["device-1"], "mf": "ACME"},
        "pl": "clicked",
        "qos": 1,
        "stype": "button_1",
        "t": "trigger/topic",
        "type": "button_short_press",
        "val_tpl": "{{ value_json.action }}",
    },
    "device_tracker": {
        **ENTITY_COMMON,
        "stat_t": "tracker/state",
        "json_attr_t": "tracker/attrs",
        "pl_rst": "None",
        "src_type": "router",
    },
    "event": {
        **ENTITY_COMMON,
        "stat_t": "event/state",
        "dev_cla": "button",
        "evt_typ": ["single_press", "double_press"],
    },
    "fan": {
        **ENTITY_COMMON,
        "cmd_t": "fan/cmd",
        "pct_cmd_t": "fan/pct/set",
        "pct_stat_t": "fan/pct/state",
        "pr_mode_cmd_t": "fan/preset/set",
        "pr_modes": ["sleep", "turbo"],
        "spd_rng_min": 1,
        "spd_rng_max": 3,
    },
    "humidifier": {
        **ENTITY_COMMON,
        "cmd_t": "humidifier/cmd",
        "hum_cmd_t": "humidifier/humidity/set",
        "hum_stat_t": "humidifier/humidity/state",
        "mode_cmd_t": "humidifier/mode/set",
        "modes": ["eco", "boost"],
        "min_hum": 35,
        "max_hum": 80,
    },
    "image": {
        **ENTITY_COMMON,
        "img_t": "image/topic",
        "img_e": "raw",
        "cont_type": "image/jpeg",
    },
    "lawn_mower": {
        **ENTITY_COMMON,
        "act_stat_t": "mower/activity",
        "dock_cmd_t": "mower/dock",
        "pause_cmd_t": "mower/pause",
        "strt_mw_cmd_t": "mower/start",
    },
    "lock": {
        **ENTITY_COMMON,
        "cmd_t": "lock/cmd",
        "stat_t": "lock/state",
        "pl_open": "OPEN",
        "pl_rst": "None",
        "stat_open": "OPEN",
        "stat_opening": "OPENING",
    },
    "notify": {
        **ENTITY_COMMON,
        "cmd_t": "notify/send",
        "cmd_tpl": "{{ value }}",
        "ret": True,
    },
    "number": {
        **ENTITY_COMMON,
        "cmd_t": "number/set",
        "stat_t": "number/state",
        "min": 5,
        "max": 20,
        "step": 0.5,
    },
    "scene": {
        **ENTITY_COMMON,
        "cmd_t": "scene/activate",
        "pl_on": "activate",
        "ret": True,
    },
    "select": {
        **ENTITY_COMMON,
        "cmd_t": "select/set",
        "stat_t": "select/state",
        "ops": ["one", "two", "three"],
    },
    "sensor": {
        **ENTITY_COMMON,
        "stat_t": "sensor/state",
        "dev_cla": "temperature",
        "unit_of_meas": "C",
        "stat_cla": "measurement",
        "sug_dsp_prc": 1,
    },
    "siren": {
        **ENTITY_COMMON,
        "cmd_t": "siren/cmd",
        "stat_t": "siren/state",
        "stat_on": "ON",
        "stat_off": "OFF",
        "av_tones": ["beep", "alarm"],
    },
    "switch": {
        **ENTITY_COMMON,
        "cmd_t": "switch/cmd",
        "stat_t": "switch/state",
        "stat_on": "ON",
        "stat_off": "OFF",
    },
    "tag": {
        "t": "tag/topic",
        "dev": {"ids": ["device-1"], "name": "Tag Device"},
        "val_tpl": "{{ value }}",
    },
    "text": {
        **ENTITY_COMMON,
        "cmd_t": "text/set",
        "stat_t": "text/state",
        "ptrn": "^[A-Z]+$",
        "min": 1,
        "max": 32,
    },
    "update": {
        **ENTITY_COMMON,
        "cmd_t": "update/install",
        "stat_t": "update/state",
        "l_ver_t": "update/latest",
        "tit": "Firmware",
        "rel_s": "Bug fixes",
    },
    "vacuum": {
        **ENTITY_COMMON,
        "cmd_t": "vacuum/cmd",
        "stat_t": "vacuum/state",
        "send_cmd_t": "vacuum/send",
        "set_fan_spd_t": "vacuum/fan",
        "fanspd_lst": ["quiet", "max"],
        "sup_feat": ["start", "stop", "return_home"],
    },
    "valve": {
        **ENTITY_COMMON,
        "cmd_t": "valve/cmd",
        "stat_t": "valve/state",
        "stat_open": "OPEN",
        "stat_clsd": "CLOSED",
    },
    "water_heater": {
        **ENTITY_COMMON,
        "mode_cmd_t": "water_heater/mode/set",
        "mode_stat_t": "water_heater/mode/state",
        "temp_cmd_t": "water_heater/temp/set",
        "temp_stat_t": "water_heater/temp/state",
        "curr_temp_t": "water_heater/current_temp",
        "pl_on": "ON",
        "pl_off": "OFF",
    },
}


@pytest.mark.parametrize("component,payload", sorted(MINIMAL_COMPONENT_PAYLOADS.items()))
def test_parse_all_minimal_components(component: str, payload: dict[str, object]) -> None:
    model = parse_component_payload(component, payload)
    assert model is not None


@pytest.mark.parametrize("component,payload", sorted(FULL_COMPONENT_PAYLOADS.items()))
def test_parse_all_full_components(component: str, payload: dict[str, object]) -> None:
    model = parse_component_payload(component, payload)
    dumped = model.model_dump(by_alias=True, exclude_none=True)
    assert dumped


def test_light_schema_dispatch_and_default() -> None:
    basic = parse_light_payload({"cmd_t": "light/cmd"})
    assert isinstance(basic, LightBasic)

    json_light = parse_light_payload({"schema": "json", "cmd_t": "light/cmd", "bri_scl": 200})
    assert isinstance(json_light, LightJson)

    template_light = parse_light_payload(
        {
            "schema": "template",
            "cmd_t": "light/cmd",
            "cmd_on_tpl": "{{ value }}",
            "cmd_off_tpl": "{{ value }}",
        }
    )
    assert isinstance(template_light, LightTemplate)


def test_registry_covers_all_supported_components() -> None:
    expected = {
        "alarm_control_panel",
        "binary_sensor",
        "button",
        "camera",
        "climate",
        "cover",
        "device_automation",
        "device_tracker",
        "event",
        "fan",
        "humidifier",
        "image",
        "lawn_mower",
        "light",
        "lock",
        "notify",
        "number",
        "scene",
        "select",
        "sensor",
        "siren",
        "switch",
        "tag",
        "text",
        "update",
        "vacuum",
        "valve",
        "water_heater",
    }
    assert expected == set(COMPONENT_MODELS)
    for component, payload in MINIMAL_COMPONENT_PAYLOADS.items():
        assert parse_component_payload(component, payload) is not None
    assert parse_component_payload("light", {"cmd_t": "light/cmd"}) is not None


def test_device_discovery_payload_parses() -> None:
    payload = {
        "dev": {"ids": ["device-1"], "name": "Device"},
        "cmps": {
            "temperature": {
                "p": "sensor",
                "uniq_id": "temperature-1",
            }
        },
        "o": {"name": "bridge"},
        "stat_t": "device/state",
    }
    parsed = parse_device_discovery_payload(payload)
    assert parsed.device.identifiers == ["device-1"]
    assert parsed.components["temperature"].platform == "sensor"


def test_invalid_qos_rejected() -> None:
    with pytest.raises(ValidationError):
        parse_component_payload("sensor", {"stat_t": "sensor/state", "qos": 3})


def test_invalid_device_info_rejected() -> None:
    with pytest.raises(ValidationError):
        parse_component_payload("sensor", {"stat_t": "sensor/state", "dev": {"name": "broken"}})


def test_conflicting_availability_rejected() -> None:
    with pytest.raises(ValidationError):
        parse_component_payload(
            "sensor",
            {
                "stat_t": "sensor/state",
                "avty": [{"t": "availability/one"}],
                "avty_t": "availability/two",
            },
        )


def test_missing_required_fields_rejected() -> None:
    with pytest.raises(ValidationError):
        parse_component_payload("button", {})
    with pytest.raises(ValidationError):
        parse_component_payload("humidifier", {})


def test_invalid_enum_rejected() -> None:
    with pytest.raises(ValidationError):
        parse_component_payload("number", {"cmd_t": "number/set", "mode": "broken"})


def test_invalid_numeric_ranges_rejected() -> None:
    with pytest.raises(ValidationError):
        parse_component_payload("fan", {"cmd_t": "fan/cmd", "spd_rng_min": 2, "spd_rng_max": 2})
    with pytest.raises(ValidationError):
        parse_component_payload("climate", {"hum_cmd_t": "climate/humidity/set", "min_hum": 90, "max_hum": 80})
    with pytest.raises(ValidationError):
        parse_component_payload("cover", {"set_pos_t": "cover/position/set"})


def test_valve_reports_position_conflict_rejected() -> None:
    with pytest.raises(ValidationError):
        parse_component_payload("valve", {"pos": True, "pl_open": "OPEN"})


def test_object_id_input_is_ignored() -> None:
    parsed = parse_component_payload(
        "sensor",
        {"stat_t": "sensor/state", "object_id": "sensor.legacy"},
    )
    dumped = parsed.model_dump(by_alias=True, exclude_none=True)
    assert "object_id" not in dumped
    assert "default_entity_id" not in dumped


def test_string_like_fields_coerce_scalar_values() -> None:
    parsed = parse_component_payload(
        "sensor",
        {
            "stat_t": 7,
            "name": 99,
            "dev": {
                "ids": [1, 2],
                "name": False,
                "mf": 123,
            },
        },
    )
    dumped = parsed.model_dump(by_alias=True, exclude_none=True)

    assert dumped["state_topic"] == "7"
    assert dumped["name"] == "99"
    assert dumped["device"]["identifiers"] == ["1", "2"]
    assert dumped["device"]["name"] == "False"
    assert dumped["device"]["manufacturer"] == "123"
