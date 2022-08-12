def dyn_import_class(dyn_module, dyn_class):
    mod = __import__(dyn_module, fromlist=[dyn_class])
    return getattr(mod, dyn_class)


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
