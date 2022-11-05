from collections import *

words = Counter(map(len, input().lower().split()))

for num, value in sorted(words.items(), key=lambda x: x[1]):
    print(f'Слов длины {num}: {value}')