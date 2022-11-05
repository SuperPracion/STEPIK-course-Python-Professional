from collections import *

words = Counter(input().lower().split())
not_popylar_products = words.most_common()[-list(words.values()).count(min(words.values())):]

print(*sorted([product[0] for product in not_popylar_products]), sep=', ')