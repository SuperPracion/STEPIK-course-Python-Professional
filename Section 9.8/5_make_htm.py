import functools

def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>' + func(*args, **kwargs) + f'</{tag}>'
        return wrapper
    return decorator