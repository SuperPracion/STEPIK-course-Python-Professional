from collections import *


def get_unicode_cost(product):
    return sum(map(ord, filter(str.isalpha, product)))


purchases = Counter(input().split(','))
max_len_purchase = max(map(len, purchases))

for purchase, value in sorted(purchases.items()):
    price = get_unicode_cost(purchase)

    print(f'{purchase}{"".ljust(max_len_purchase - len(purchase))}: {price} UC x {value} = {price * value} UC')