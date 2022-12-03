import string
from itertools import *

def alnum_sequence():
    for alnums in cycle(zip(count(1), string.ascii_uppercase)):
        yield from alnums

alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))