import functools

def takes(*datatypes):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not all([type(arg) in datatypes for arg in (*args, *kwargs.values())]):
                raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return decorator