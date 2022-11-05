from collections import *

words = Counter(sorted(input().lower().split(), reverse=True))

print(words.most_common(1)[0][0])