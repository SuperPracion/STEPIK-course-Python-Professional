from itertools import *

iterable = input()

for tpl in sorted(set(permutations(iterable))):
    print(''.join(tpl))

