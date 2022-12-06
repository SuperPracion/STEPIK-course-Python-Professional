from itertools import *

def ranges(numbers):
    res = []
    for _, group in groupby(numbers, key=lambda n: n - numbers.index(n)):
        group = tuple(group)
        group = group[0], group[-1]
        res.append((group))

    return res


numbers = [1, 2, 3, 4, 5, 6, 7]

print(ranges(numbers))