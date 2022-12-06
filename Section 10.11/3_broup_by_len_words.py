from itertools import *

group_iter = groupby(sorted(input().split(), key=len), key=len)

for length, words in group_iter:
    print(f'{length} -> {", ".join(sorted(words))}')