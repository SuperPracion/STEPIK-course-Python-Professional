import functools


def add_attrs(**kwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.__dict__.update(kwargs)
        return wrapper
    return decorator


@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)
