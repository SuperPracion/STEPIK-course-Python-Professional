import functools


def ignore_exception(*ignore_exceps):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ignore_exceps as err:
                print(f'Исключение {err.__class__.__name__} обработано')
        return wrapper
    return decorator


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x


f(0)
