from __future__ import annotations

from typing import Any

from ha_mqtt_models_pydantic.discovery import parse_component_payload

ZWAVE_SWITCH_DISCOVERY_PAYLOAD: dict[str, Any] = {
    "payload_off": False,
    "payload_on": True,
    "value_template": "{{ value_json.value }}",
    "command_topic": "zwave/nodeID_4/switch_binary/endpoint_0/targetValue/set",
    "state_topic": "zwave/nodeID_4/switch_binary/endpoint_0/currentValue",
    "availability": [
        {
            "payload_available": "true",
            "payload_not_available": "false",
            "topic": "zwave/nodeID_4/status",
            "value_template": "{{'true' if value_json.value else 'false'}}",
        },
        {
            "topic": "zwave/_CLIENTS/ZWAVE_GATEWAY-zwave-js-ui/status",
            "value_template": "{{'online' if value_json.value else 'offline'}}",
        },
        {
            "payload_available": "true",
            "payload_not_available": "false",
            "topic": "zwave/driver/status",
        },
    ],
    "availability_mode": "all",
    "device": {
        "identifiers": ["zwavejs2mqtt_0xc5e72b9d_node4"],
        "manufacturer": "Shenzhen Neo Electronics Co., Ltd.",
        "model": "Wall Plug Switch (NAS-WR01ZE)",
        "name": "nodeID_4",
        "sw_version": "2.23.0",
    },
    "name": "nodeID_4_switch",
    "unique_id": "zwavejs2mqtt_0xc5e72b9d_4-37-0-currentValue",
}

ZWAVE_BINARY_SENSOR_DISCOVERY_PAYLOAD: dict[str, Any] = {
    "payload_on": 22,
    "payload_off": 23,
    "value_template": "{{ value_json.value }}",
    "device_class": "door",
    "state_topic": "zwave/nodeID_7/notification/endpoint_0/Access_Control/Door_state_simple",
    "availability": [
        {
            "payload_available": "true",
            "payload_not_available": "false",
            "topic": "zwave/nodeID_7/status",
            "value_template": "{{'true' if value_json.value else 'false'}}",
        },
        {
            "topic": "zwave/_CLIENTS/ZWAVE_GATEWAY-zwave-js-ui/status",
            "value_template": "{{'online' if value_json.value else 'offline'}}",
        },
        {
            "payload_available": "true",
            "payload_not_available": "false",
            "topic": "zwave/driver/status",
        },
    ],
    "availability_mode": "all",
    "json_attributes_topic": "zwave/nodeID_7/notification/endpoint_0/Access_Control/Door_state_simple",
    "device": {
        "identifiers": ["zwavejs2mqtt_0xc5e72b9d_node7"],
        "manufacturer": "Shenzhen Neo Electronics Co., Ltd.",
        "model": "Door/Window Sensor (NAS-DS01Z)",
        "name": "nodeID_7",
        "sw_version": "2.12.0",
    },
    "name": "nodeID_7_door_state_simple",
    "unique_id": "zwavejs2mqtt_0xc5e72b9d_7-113-0-Access_Control-Door_state_simple",
}


def test_zwave_switch_discovery_payload_parses() -> None:
    parsed = parse_component_payload("switch", ZWAVE_SWITCH_DISCOVERY_PAYLOAD)
    dumped = parsed.model_dump(by_alias=True, exclude_none=True)

    assert dumped["payload_off"] == "False"
    assert dumped["payload_on"] == "True"
    assert dumped["availability_mode"] == "all"
    assert len(dumped["availability"]) == 3
    assert dumped["device"]["identifiers"] == ["zwavejs2mqtt_0xc5e72b9d_node4"]
    assert dumped["unique_id"] == "zwavejs2mqtt_0xc5e72b9d_4-37-0-currentValue"


def test_zwave_binary_sensor_discovery_payload_parses() -> None:
    parsed = parse_component_payload("binary_sensor", ZWAVE_BINARY_SENSOR_DISCOVERY_PAYLOAD)
    dumped = parsed.model_dump(by_alias=True, exclude_none=True)

    assert dumped["payload_off"] == "23"
    assert dumped["payload_on"] == "22"
    assert dumped["availability_mode"] == "all"
    assert dumped["device_class"] == "door"
    assert dumped["json_attributes_topic"] == "zwave/nodeID_7/notification/endpoint_0/Access_Control/Door_state_simple"
    assert dumped["device"]["identifiers"] == ["zwavejs2mqtt_0xc5e72b9d_node7"]
    assert dumped["unique_id"] == "zwavejs2mqtt_0xc5e72b9d_7-113-0-Access_Control-Door_state_simple"
