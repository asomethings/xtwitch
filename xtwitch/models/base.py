from __future__ import annotations

from xtwitch.models import attr
from xtwitch.models.manager import Manager


class ModelMetaClass(attr.AttrsMetaClass):

    def __new__(mcs, name, bases, attrs, **kwargs):
        if 'manager' not in attrs:
            raise Exception

        if not isinstance(attrs['manager'], Manager):
            raise Exception

        obj = super(ModelMetaClass, mcs).__new__(mcs, name, bases, attrs)
        return obj


class Model(attr.S, metaclass=ModelMetaClass):
    manager = Manager()
