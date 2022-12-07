from itertools import *

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

res = 0
for banknotes in range(1, 22):
    for tpl in set(combinations(wallet, r=banknotes)):
        if sum(tpl) == 100:
            res += 1

print(res)