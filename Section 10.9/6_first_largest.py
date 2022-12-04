from itertools import *

def first_largest(iterable, number):
    for index, num in enumerate(iterable):
        if num >= number:
            return index
    return -1


numbers = [10, 2, 14, 7, 7, 18, 20]

print(first_largest(numbers, 11))
