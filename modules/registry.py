# coding: utf-8
# third party imports
from flask import g, has_app_context


class Registry(object):
    _objects = {}
    model_registered_keys = ['current-user', 'current-role']

    @staticmethod
    def register(key, obj, in_g=False):
        if in_g:
            setattr(g, key, obj)
        else:
            Registry._objects[key] = obj

    @staticmethod
    def registered(key, default=None):
        def registered(key, default):
            is_model = key in Registry.model_registered_keys
            obj = None

            if is_model:
                obj = getattr(g, key) if hasattr(g, key) else Registry._objects.get(key, default)
            elif hasattr(g, key):
                return getattr(g, key)
            elif key in Registry._objects:
                return Registry._objects[key]

            if is_model:
                if obj:
                    obj.link_to_session()
                    return obj
                if default:
                    print(default)
                    default.link_to_session()

            return default

        if not has_app_context():
            from transport.flask import TasksTransport

            with TasksTransport.app.app_context():
                return registered(key, default)

        return registered(key, default)

    @staticmethod
    def remove(key):
        if hasattr(g, key):
            delattr(g, key)
        elif key in Registry._objects:
            del Registry._objects[key]
