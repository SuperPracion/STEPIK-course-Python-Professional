import functools

def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if not type(res) == datatype:
                raise TypeError
            return res
        return wrapper
    return decorator
