import inspect

from xtwitch.models.manager import Manager


class ModelMetaClass(type):

    def __new__(mcs, name, bases, attrs, **kwargs):
        new_object: ModelMetaClass = super(ModelMetaClass, mcs).__new__(mcs, name, bases, attrs)
        new_object._setup_manager()
        return new_object

    def _setup_manager(cls) -> None:
        manager_name = f'{cls.__name__}{Manager.__name__}'
        manager_methods = cls._get_methods()
        manager = type(manager_name, (Manager,), manager_methods)
        setattr(cls, 'manager', manager())

    def _get_methods(cls) -> dict:
        methods = dict()
        members = inspect.getmembers(cls, predicate=inspect.isfunction)
        for name, method in members:
            is_private = getattr(method, 'is_private', None)
            if is_private:
                continue

            if is_private is None and name.startswith('_'):
                continue

            methods[name] = method

        return methods


class Model(metaclass=ModelMetaClass):
    pass

