from itertools import *


def roundrobin(*args):
    yield from (elem
                for pairs in zip_longest(*args, fillvalue='')
                for elem in pairs if elem != '')


numbers = [1, 2, 3]
letters = iter('beegeek')

print(*roundrobin(numbers, letters))
