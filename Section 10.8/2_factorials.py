import itertools
import operator

def factorials(n):
    return itertools.accumulate(range(1, n + 1), operator.mul)

numbers = factorials(6)

print(*numbers)