import functools
class MaxRetriesException(Exception):
    pass

def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except:
                    continue
            else:
                raise MaxRetriesException
        return wrapper
    return decorator