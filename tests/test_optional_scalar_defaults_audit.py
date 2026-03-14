from __future__ import annotations

from typing import get_args

import pytest
from pydantic import BaseModel

from ha_mqtt_models_pydantic.components import Cover, Humidifier, Valve

NULLABLE_EXCEPTIONS = [
    (Cover, "payload_close"),
    (Cover, "payload_open"),
    (Cover, "payload_stop"),
    (Cover, "payload_stop_tilt"),
    (Valve, "payload_close"),
    (Valve, "payload_open"),
    (Humidifier, "device_class"),
]

NULLABLE_EXCEPTION_IDS = [f"{model.__name__}.{field}" for model, field in NULLABLE_EXCEPTIONS]


@pytest.mark.parametrize(("model", "field"), NULLABLE_EXCEPTIONS, ids=NULLABLE_EXCEPTION_IDS)
def test_nullable_exceptions_remain_optional(model: type[BaseModel], field: str) -> None:
    assert type(None) in get_args(model.model_fields[field].annotation)
    assert model.model_fields[field].default is not None
