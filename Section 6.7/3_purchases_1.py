from collections import *

purchases = Counter(input().split(','))

for purchase, value in sorted(purchases.items()):
    print(f'{purchase}: {value}')