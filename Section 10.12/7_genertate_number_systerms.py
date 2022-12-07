import string
from itertools import *


def generate_num_of_system_numbers(n, m):
    nums_generate = (string.digits + string.ascii_uppercase)[:2]

    return product(nums_generate, repeat=m)


for comb in generate_num_of_system_numbers(2, 3):
    print(''.join(comb), end=' ')
