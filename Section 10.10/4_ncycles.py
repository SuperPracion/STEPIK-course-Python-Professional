from itertools import *

def ncycles(iterable, time):
    return chain.from_iterable(tee(iterable, time))

iterator = iter([1])

print(*ncycles(iterator, 10))