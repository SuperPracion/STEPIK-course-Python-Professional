from itertools import *

def is_rising(iterable):
    return all(f < s for f, s in pairwise(iterable))

iterator = iter(list(range(100, 200)))

print(is_rising(iterator))