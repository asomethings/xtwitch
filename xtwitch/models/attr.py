from typing import Callable

import attr

from xtwitch.models.base import JsonParser


def optional(converter: Callable, *args, **kwargs):
    if converter is issubclass(converter, JsonParser):
        converter = converter.from_json

    return attr.ib(converter=attr.converters.optional(converter), default=None, *args, **kwargs)


def attrs(*args, **kwargs):
    return attr.s(kw_only=True, auto_attribs=True, *args, **kwargs)


s = attrs
