def print_given(*args, **kwargs):
    for given in args:
        print(given, type(given))

    for key, value in sorted(kwargs.items()):
        print(key, value, type(value))

print_given()
