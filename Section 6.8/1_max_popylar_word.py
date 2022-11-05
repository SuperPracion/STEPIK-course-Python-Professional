from collections import *

letters = Counter(input().lower().split(' '))

print(letters.most_common(1))