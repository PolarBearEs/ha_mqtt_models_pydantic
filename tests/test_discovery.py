from __future__ import annotations

from typing import Any

import pytest
from pydantic import ValidationError

from ha_mqtt_models_pydantic.components.infrared import InfraredEmitter, InfraredReceiver
from ha_mqtt_models_pydantic.components.light import LightBasic, LightJson, LightTemplate
from ha_mqtt_models_pydantic.discovery import (
    COMPONENT_MODELS,
    parse_component_payload,
    parse_device_discovery_payload,
    parse_infrared_payload,
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
    "date": {"cmd_t": "date/set"},
    "datetime": {"cmd_t": "datetime/set"},
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
    "infrared": {"schema": "emitter", "cmd_t": "infrared/send"},
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
    "time": {"cmd_t": "time/set"},
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
    "date": {
        **ENTITY_COMMON,
        "cmd_t": "date/set",
        "cmd_tpl": "{{ value }}",
        "stat_t": "date/state",
        "val_tpl": "{{ value_json.date }}",
    },
    "datetime": {
        **ENTITY_COMMON,
        "cmd_t": "datetime/set",
        "stat_t": "datetime/state",
        "tz": "Europe/Madrid",
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
        "stop_cmd_t": "mower/stop",
        "stop_cmd_tpl": "{{ value }}",
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
    "infrared": {
        **ENTITY_COMMON,
        "schema": "receiver",
        "stat_t": "infrared/received",
        "val_tpl": "{{ value_json }}",
    },
    "text": {
        **ENTITY_COMMON,
        "cmd_t": "text/set",
        "stat_t": "text/state",
        "ptrn": "^[A-Z]+$",
        "min": 1,
        "max": 32,
    },
    "time": {
        **ENTITY_COMMON,
        "cmd_t": "time/set",
        "stat_t": "time/state",
        "ret": True,
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
        "cln_segmnts_cmd_t": "vacuum/clean_segments",
        "cln_segmnts_cmd_tpl": "{{ value | tojson }}",
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
        "date",
        "datetime",
        "device_automation",
        "device_tracker",
        "event",
        "fan",
        "humidifier",
        "image",
        "infrared",
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
        "time",
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


def test_new_platforms_require_command_topic() -> None:
    for component in ("date", "datetime", "time"):
        with pytest.raises(ValidationError):
            parse_component_payload(component, {"stat_t": f"{component}/state"})


def test_datetime_timezone_expanded() -> None:
    parsed = parse_component_payload("datetime", {"cmd_t": "datetime/set", "tz": "UTC"})
    assert parsed.model_dump()["timezone"] == "UTC"


def test_infrared_schema_dispatch() -> None:
    emitter = parse_infrared_payload({"schema": "emitter", "cmd_t": "infrared/send", "ret": True})
    assert isinstance(emitter, InfraredEmitter)
    assert emitter.retain is True

    receiver = parse_component_payload("infrared", {"schema": "receiver", "stat_t": "infrared/received"})
    assert isinstance(receiver, InfraredReceiver)


def test_infrared_invalid_payloads_rejected() -> None:
    with pytest.raises(ValueError, match="unsupported infrared schema"):
        parse_infrared_payload({"cmd_t": "infrared/send"})
    with pytest.raises(ValidationError):
        parse_infrared_payload({"schema": "emitter", "stat_t": "infrared/received"})
    with pytest.raises(ValidationError):
        parse_infrared_payload({"schema": "receiver", "cmd_t": "infrared/send"})


def test_visible_by_default() -> None:
    assert parse_component_payload("sensor", {"stat_t": "sensor/state"}).model_dump()["visible_by_default"] is True
    parsed = parse_component_payload("sensor", {"stat_t": "sensor/state", "vis": False})
    assert parsed.model_dump()["visible_by_default"] is False


@pytest.mark.parametrize(
    "value,expected",
    [
        (30, 30),
        (0, 0),
        (True, 1),
        (False, 0),
        ({"minutes": 1, "seconds": 5}, 65),
        ({"hours": 1.5}, 5400),
        ({"milliseconds": 1500}, 1),
    ],
)
def test_message_expiry_interval_parses(value: object, expected: int) -> None:
    parsed = parse_component_payload("switch", {"cmd_t": "switch/cmd", "msg_exp_int": value})
    assert parsed.model_dump()["message_expiry_interval"] == expected


@pytest.mark.parametrize(
    "value",
    [
        -1,
        "30",
        1.5,
        {},
        {"weeks": 1},
        {"seconds": -5},
        {"seconds": "x"},
        {"seconds": 1e100},
        {"seconds": float("inf")},
        {"seconds": float("nan")},
        None,
    ],
)
def test_message_expiry_interval_rejected(value: object) -> None:
    with pytest.raises(ValidationError):
        parse_component_payload("switch", {"cmd_t": "switch/cmd", "msg_exp_int": value})


def test_device_discovery_message_expiry_interval() -> None:
    parsed = parse_device_discovery_payload(
        {
            "dev": {"ids": ["device-1"]},
            "o": {"name": "bridge"},
            "cmps": {"temperature": {"p": "sensor", "uniq_id": "temperature-1", "stat_t": "device/temperature"}},
            "msg_exp_int": {"hours": 1},
        }
    )
    assert parsed.message_expiry_interval == 3600
    with pytest.raises(ValidationError):
        parse_device_discovery_payload(
            {
                "dev": {"ids": ["device-1"]},
                "o": {"name": "bridge"},
                "cmps": {"temperature": {"p": "sensor", "uniq_id": "temperature-1", "stat_t": "device/temperature"}},
                "msg_exp_int": None,
            }
        )


def test_lawn_mower_stop_command() -> None:
    parsed = parse_component_payload("lawn_mower", {"stop_cmd_t": "mower/stop", "stop_cmd_tpl": "{{ value }}"})
    dumped = parsed.model_dump()
    assert dumped["stop_command_topic"] == "mower/stop"
    assert dumped["stop_command_template"] == "{{ value }}"


def test_vacuum_clean_segments_requires_unique_id() -> None:
    parsed = parse_component_payload("vacuum", {"cln_segmnts_cmd_t": "vacuum/segments", "uniq_id": "vacuum-1"})
    assert parsed.model_dump()["clean_segments_command_topic"] == "vacuum/segments"
    with pytest.raises(ValidationError, match="requires unique_id"):
        parse_component_payload("vacuum", {"cln_segmnts_cmd_t": "vacuum/segments"})


@pytest.mark.parametrize(
    "value,expected",
    [
        (True, True),
        (False, False),
        (1, True),
        (0, False),
        (2, True),
        (-1, True),
        (1.5, True),
        (0.0, False),
        ("enable", True),
        ("disable", False),
        (" ON ", True),
        ("No", False),
    ],
)
def test_new_boolean_fields_follow_home_assistant(value: object, expected: bool) -> None:
    sensor = parse_component_payload("sensor", {"stat_t": "sensor/state", "vis": value})
    assert sensor.model_dump()["visible_by_default"] is expected
    emitter = parse_infrared_payload({"schema": "emitter", "cmd_t": "infrared/send", "ret": value})
    assert isinstance(emitter, InfraredEmitter)
    assert emitter.retain is expected


@pytest.mark.parametrize("value", ["maybe", "", "t", "f", "y", "n", None, [], {}])
def test_new_boolean_fields_reject_invalid_values(value: object) -> None:
    with pytest.raises(ValidationError):
        parse_component_payload("sensor", {"stat_t": "sensor/state", "vis": value})
    with pytest.raises(ValidationError):
        parse_infrared_payload({"schema": "emitter", "cmd_t": "infrared/send", "ret": value})


# Each new publish topic field with the payload it needs to be otherwise valid
NEW_PUBLISH_TOPIC_FIELDS = [
    ("date", {}, "cmd_t"),
    ("datetime", {}, "cmd_t"),
    ("time", {}, "cmd_t"),
    ("infrared", {"schema": "emitter"}, "cmd_t"),
    ("lawn_mower", {}, "stop_cmd_t"),
    ("vacuum", {"uniq_id": "vacuum-1"}, "cln_segmnts_cmd_t"),
]


@pytest.mark.parametrize("component,payload,key", NEW_PUBLISH_TOPIC_FIELDS)
@pytest.mark.parametrize("topic", ["a/b", "/", "a//b", "é/ü"])
def test_new_publish_topics_accepted(component: str, payload: dict[str, object], key: str, topic: str) -> None:
    parse_component_payload(component, {**payload, key: topic})


@pytest.mark.parametrize("component,payload,key", NEW_PUBLISH_TOPIC_FIELDS)
@pytest.mark.parametrize("topic", ["", "a/+/b", "a/#", "#", "a\x01", "a\x85", "a\ufdd0", "a\0", "\ud800", "x" * 65536])
def test_new_publish_topics_rejected(component: str, payload: dict[str, object], key: str, topic: str) -> None:
    with pytest.raises(ValidationError):
        parse_component_payload(component, {**payload, key: topic})


@pytest.mark.parametrize("topic", ["a/b", "#", "+", "a/#", "/#", "+/a/+", "a/+/b"])
def test_infrared_receiver_subscribe_topic_accepted(topic: str) -> None:
    parse_infrared_payload({"schema": "receiver", "stat_t": topic})


@pytest.mark.parametrize("topic", ["", "a/#/b", "a#", "#/a", "a+/b", "a/b+", "a\x01"])
def test_infrared_receiver_subscribe_topic_rejected(topic: str) -> None:
    with pytest.raises(ValidationError):
        parse_infrared_payload({"schema": "receiver", "stat_t": topic})


@pytest.mark.parametrize(
    "component,payload,key",
    [
        ("date", {"cmd_t": "date/set"}, "cmd_tpl"),
        ("datetime", {"cmd_t": "datetime/set"}, "tz"),
        ("time", {"cmd_t": "time/set"}, "val_tpl"),
        ("infrared", {"schema": "emitter", "cmd_t": "infrared/send"}, "cmd_tpl"),
        ("infrared", {"schema": "receiver", "stat_t": "infrared/received"}, "val_tpl"),
        ("lawn_mower", {}, "stop_cmd_t"),
        ("lawn_mower", {}, "stop_cmd_tpl"),
        ("vacuum", {"uniq_id": "vacuum-1"}, "cln_segmnts_cmd_t"),
        ("vacuum", {}, "cln_segmnts_cmd_tpl"),
    ],
)
def test_new_optional_fields_reject_explicit_null(component: str, payload: dict[str, object], key: str) -> None:
    parse_component_payload(component, payload)
    with pytest.raises(ValidationError):
        parse_component_payload(component, {**payload, key: None})
