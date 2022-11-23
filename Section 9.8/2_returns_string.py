import functools

def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)

        if not type(res) == str:
            raise TypeError

        return res
    return wrapper