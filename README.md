# ha-mqtt-models-pydantic

Typed Pydantic v2 models for Home Assistant MQTT discovery payloads.

This library validates Home Assistant MQTT discovery payloads as plain Python data, without depending on Home Assistant itself. It is useful when you want to inspect, validate, transform, or generate discovery payloads before publishing them to MQTT.

## What It Includes

- Pydantic models for Home Assistant MQTT discovery components
- Helpers to parse raw discovery payloads into the right model
- Support for Home Assistant discovery abbreviations such as `stat_t`, `cmd_t`, and `dev`
- Dedicated light parsing for `basic`, `json`, and `template` schemas
- Typed shared models for entity metadata, device info, and origin info

## Installation

From PyPI:

```bash
pip install ha-mqtt-models-pydantic
```

With `uv`:

```bash
uv add ha-mqtt-models-pydantic
```

## Quick Start

```python
from ha_mqtt_models_pydantic import parse_component_payload

payload = {
    "dev_cla": "temperature",
    "name": "Living Room Temperature",
    "stat_t": "homeassistant/sensor/living_room_temperature/state",
    "unit_of_meas": "°C",
    "val_tpl": "{{ value_json.temperature }}",
    "def_ent_id": "sensor.living_room_temperature",
    "dev": {
        "ids": ["living_room_sensor_01"],
        "name": "Living Room Sensor",
    },
}

sensor = parse_component_payload("sensor", payload)

print(sensor.name)
print(sensor.state_topic)
print(sensor.device.identifiers)
```

`parse_component_payload()` expands Home Assistant abbreviations before validation, so both abbreviated and expanded payloads are accepted.

## Main APIs

### Parse a component payload

```python
from ha_mqtt_models_pydantic import parse_component_payload

switch = parse_component_payload(
    "switch",
    {
        "cmd_t": "devices/lamp/set",
        "stat_t": "devices/lamp/state",
        "pl_on": "ON",
        "pl_off": "OFF",
        "uniq_id": "lamp_switch_01",
    },
)
```

### Parse a light payload

```python
from ha_mqtt_models_pydantic import parse_light_payload

light = parse_light_payload(
    {
        "schema": "json",
        "cmd_t": "devices/light/set",
        "stat_t": "devices/light/state",
        "name": "Desk Light",
    }
)
```

### Parse a device discovery payload

```python
from ha_mqtt_models_pydantic import parse_device_discovery_payload

device_payload = parse_device_discovery_payload(
    {
        "dev": {"ids": ["device_01"], "name": "Example Device"},
        "o": {"name": "example-generator"},
        "cmps": {
            "temperature": {
                "p": "sensor",
                "dev_cla": "temperature",
                "stat_t": "devices/example/temperature",
                "unit_of_meas": "°C",
            }
        },
    }
)
```

## Supported Components

- `alarm_control_panel`
- `binary_sensor`
- `button`
- `camera`
- `climate`
- `cover`
- `device_automation`
- `device_tracker`
- `event`
- `fan`
- `humidifier`
- `image`
- `lawn_mower`
- `light`
- `lock`
- `notify`
- `number`
- `scene`
- `select`
- `sensor`
- `siren`
- `switch`
- `tag`
- `text`
- `update`
- `vacuum`
- `valve`
- `water_heater`

## Notes

- The import package is `ha_mqtt_models_pydantic`.
- The PyPI distribution name is `ha-mqtt-models-pydantic`.
- The library targets Python `3.11+`.
- The package is marked as typed with `py.typed`.

## Development

Install development dependencies:

```bash
uv sync --dev
```

Run checks:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy .
uv run pytest -q
```

## License

MIT
