from collections import *

books = Counter(input().split(' '))
total = 0

for _ in range(int(input())):
    need_class, price = input().split()
    if books[need_class] > 0:
        total += int(price)
        books[need_class] -= 1

print(total)

