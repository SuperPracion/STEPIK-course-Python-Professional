from itertools import *

def take(iterable, n):
    yield from islice(iterable, n)

iterator = iter('beegeek')

print(*take(iterator, 1))