import functools

def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res[:start] + f'{char * ((len(res) if end > len(res) else end) - start)}' + res[end:]
        return wrapper
    return decorator