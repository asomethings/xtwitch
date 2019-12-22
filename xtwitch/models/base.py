import inspect

from xtwitch.models.manager import Manager


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
