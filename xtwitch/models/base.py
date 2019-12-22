from __future__ import annotations

import attr

from xtwitch.models.manager import Manager


class JsonParser:

    @classmethod
    def from_json(cls, data: dict) -> JsonParser:
        if not attr.has(cls):
            raise Exception

        filtered_dict = dict()
        for k, v in data.items():
            if k not in cls.__annotations__.keys():
                continue

            filtered_dict.update({k: v})

        return cls(**filtered_dict)


class ModelMetaClass(type):

    def __new__(mcs, name, bases, attrs, **kwargs):
        if 'manager' not in attrs:
            raise Exception

        if not isinstance(attrs['manager'], Manager):
            raise Exception

        obj = super(ModelMetaClass, mcs).__new__(mcs, name, bases, attrs)
        return attr.s(kw_only=True)(obj)


class Model(JsonParser, metaclass=ModelMetaClass):
    manager = Manager()
