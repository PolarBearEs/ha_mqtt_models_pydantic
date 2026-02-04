# Home Assistant MQTT Pydantic Models

Pydantic models for Home Assistant MQTT discovery payloads. This project provides a set of robust, type-safe models to validate and work with MQTT discovery data in Home Assistant.

## Features

- **Pydantic V2**: Leveraging the latest Pydantic features for high-performance validation.
- **Type Safety**: Full type hinting for MQTT discovery payloads.
- **Centralized Constants**: All MQTT configuration keys and default values are centralized in `ha_mqtt_models_pydantic/const.py`, mirroring Home Assistant core conventions.
- **Abbreviation Expansion**: Helper tools to expand abbreviated MQTT discovery keys.
- **Comprehensive Coverage**: Supporting a wide range of Home Assistant entities (Sensor, Climate, Light, Lock, Vacuum, etc.).

## Installation

```bash
uv pip install .
```

## Usage

### Validating a Discovery Payload

```python
from ha_mqtt_models_pydantic.discovery import parse_component_payload

# Example MQTT discovery payload (abbreviated)
payload = {
    "dev_cla": "temperature",
    "name": "Temperature",
    "stat_t": "homeassistant/sensor/temp/state",
    "unit_of_meas": "°C",
    "val_tpl": "{{ value_json.temperature }}",
    "def_ent_id": "sensor.temperature",
    "dev": {
        "ids": ["temp_sensor_01"],
        "name": "Living Room Sensor"
    }
}

# Expand abbreviations and validate with the correct component model
sensor = parse_component_payload("sensor", payload)

print(sensor.name)
# Output: Temperature
```

### Using Constants

```python
from ha_mqtt_models_pydantic.const import CONF_STATE_TOPIC, DEFAULT_PAYLOAD_AVAILABLE

print(f"Discovery key for state topic: {CONF_STATE_TOPIC}")
print(f"Default online payload: {DEFAULT_PAYLOAD_AVAILABLE}")
```

## Supported Components

- Alarm Control Panel
- Binary Sensor
- Button
- Camera
- Climate
- Cover
- Device Tracker
- Event
- Fan
- Humidifier
- Image
- Lawn Mower
- Light
- Lock
- Notify
- Number
- Scene
- Select
- Sensor
- Siren
- Switch
- Tag
- Text
- Update
- Vacuum
- Valve
- Water Heater

## Development

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv)

### Running Verification

You can verify the models against the vendored Home Assistant snapshot with:

```bash
./.venv/bin/python -m pytest
```

### Code Quality

The project uses `ruff` for linting and formatting. Line length is configured to 120 characters.

```bash
ruff check .
ruff format .
```

## License

MIT
