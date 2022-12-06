from itertools import *


def group_anagrams(words):
    group_iter = groupby(sorted(words, key=sorted), key=sorted)
    for group, words in group_iter:
        yield tuple(words)


groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])

print(*groups)
