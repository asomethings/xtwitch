from __future__ import annotations

import inspect
from typing import Callable

import attr


def optional(converter: Callable, *args, **kwargs):
    if inspect.isclass(converter) and issubclass(converter, Attrs):
        converter = converter.from_json

    return attr.ib(converter=attr.converters.optional(converter), default=None, *args, **kwargs)


class AttrsMetaClass(type):

    def __new__(mcs, *args, **kwargs):
        obj = super(AttrsMetaClass, mcs).__new__(mcs, *args, **kwargs)
        return attr.s(kw_only=True, auto_attribs=True)(obj)


class Attrs(metaclass=AttrsMetaClass):

    @classmethod
    def from_json(cls, data: dict) -> Attrs:
        if not attr.has(cls):
            raise Exception

        filtered_dict = dict()
        for k, v in data.items():
            if k not in cls.__annotations__.keys():
                continue

            filtered_dict.update({k: v})

        return cls(**filtered_dict)


S = Attrs
