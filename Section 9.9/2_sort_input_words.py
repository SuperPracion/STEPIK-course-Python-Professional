import functools
import sys

@functools.cache
def sort_word(word):
    return ''.join(sorted(word.strip()))

for word in sys.stdin:
    print(word)