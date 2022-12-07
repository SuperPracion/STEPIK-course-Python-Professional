from itertools import *

wallet = [100, 50, 20, 10, 5]

cash = set()
for banknotes in range(1, 22):
    for tpl in combinations_with_replacement(wallet, r=banknotes):
        if sum(tpl) == 100:
            cash.add(tpl)

print(len(cash))