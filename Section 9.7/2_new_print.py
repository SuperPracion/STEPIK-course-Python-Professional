def dec(func):
    def wrapper(*args, **kwargs):
        args = [str(arg).upper() for arg in args]
        kwargs = {str(k).upper(): v for k, v in kwargs.items()}
        return new_print(*args, sep=kwargs.get('sep', ' '), end=kwargs.get('end', '\n'))

    return wrapper

new_print = print
print = dec(print)