from itertools import *


def grouper(iterable, n):
    iters = iter(iterable)
    return zip_longest(*[iters] * n)


iterator = iter([1, 2, 3])

print(*grouper(iterator, 5))
