import string


def is_lower(x):
    return x in string.ascii_lowercase


def is_upper(x):
    return x in string.ascii_uppercase


def is_even(x):
    return x in string.digits and int(x) % 2 == 0


def is_odd(x):
    return x in string.digits and int(x) % 2 == 1


str = sorted(input())
print(*sorted(str, key=lambda x: ( is_even(x), is_odd(x), is_upper(x), is_lower(x))), sep='')
