from itertools import *


def first_true(iterable, predicate):
    if predicate is None:
        predicate = bool

    return next(dropwhile(lambda x: not predicate(x), iterable), None)



numbers = [1, 1, 1, 1, 2, 4, 5, 6]

print(first_true(numbers, lambda num: num % 2 == 0))
