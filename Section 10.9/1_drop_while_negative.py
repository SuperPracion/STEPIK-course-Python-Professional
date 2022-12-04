from itertools import *


def drop_while_negative(iterable):
    yield from dropwhile(lambda x: x < 0, iterable)


iterator = iter([-3, -2, -1, -4, -5, -6])

print(list(drop_while_negative(iterator)))
