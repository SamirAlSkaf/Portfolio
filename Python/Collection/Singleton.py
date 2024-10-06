_instance = None
_lock = object()

def get_instance(cls, *args, **kwargs):
    global _instance
    with _lock:
        if _instance is None:
            _instance = cls(*args, **kwargs)
    return _instance
