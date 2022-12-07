from itertools import *

def password_gen():
    for nums in product(range(10), repeat=3):
        yield ''.join(map(str,nums))


print(*password_gen())