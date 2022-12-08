import string
from itertools import *


def generate_num_of_system_numbers(n, m):
    nums_generate = (string.digits + string.ascii_uppercase)[:n]

    return product(nums_generate, repeat=m)


for comb in generate_num_of_system_numbers(int(input()), int(input())):
    print(''.join(comb), end=' ')
