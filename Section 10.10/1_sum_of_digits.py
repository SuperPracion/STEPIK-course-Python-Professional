from itertools import *

def sum_of_digits(iterable):
    strings = map(str, iterable)
    all_elements = chain.from_iterable(strings)
    int_digits = map(int, all_elements)
    return sum(int_digits)

print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))