from itertools import *


def drop_this(iterable, obj):
    yield from dropwhile(lambda x: x == obj, iterable)


iterator = iter('bbbbeebee')

print(*drop_this(iterator, 'b'))
