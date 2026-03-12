from __future__ import annotations

from types import UnionType
from typing import Annotated, Any, Union, get_args, get_origin


def _strip_annotated(annotation: Any) -> Any:
    while get_origin(annotation) is Annotated:
        annotation = get_args(annotation)[0]
    return annotation


def _is_union(annotation: Any) -> bool:
    return get_origin(annotation) in (UnionType, Union)


def _non_none_union_args(annotation: Any) -> list[Any]:
    return [arg for arg in get_args(annotation) if arg is not type(None)]


def is_string_like_annotation(annotation: Any) -> bool:
    annotation = _strip_annotated(annotation)

    if annotation is str:
        return True

    if _is_union(annotation):
        return any(is_string_like_annotation(arg) for arg in _non_none_union_args(annotation))

    if get_origin(annotation) is list:
        args = get_args(annotation)
        return len(args) == 1 and is_string_like_annotation(args[0])

    return False


def _coerce_scalar_to_string(value: Any) -> Any:
    if value is None or isinstance(value, str):
        return value
    if isinstance(value, (list, dict)):
        return value
    return str(value)


def coerce_string_like_value(value: Any, annotation: Any) -> Any:
    annotation = _strip_annotated(annotation)

    if annotation is str:
        return _coerce_scalar_to_string(value)

    if _is_union(annotation):
        for arg in _non_none_union_args(annotation):
            if is_string_like_annotation(arg):
                return coerce_string_like_value(value, arg)
        return value

    if get_origin(annotation) is list and isinstance(value, list):
        (item_annotation,) = get_args(annotation)
        return [coerce_string_like_value(item, item_annotation) for item in value]

    return value


def coerce_string_like_fields(model_fields: dict[str, Any], data: Any) -> Any:
    if not isinstance(data, dict):
        return data

    coerced = dict(data)
    for field_name, field in model_fields.items():
        if not is_string_like_annotation(field.annotation):
            continue

        for key in {field_name, field.alias} - {None}:
            if key in coerced:
                coerced[key] = coerce_string_like_value(coerced[key], field.annotation)

    return coerced
