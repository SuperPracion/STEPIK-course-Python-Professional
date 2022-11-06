from collections import *

def scrabble(symbols, word):
    return Counter(word.lower()) <= Counter(symbols.lower())

print(scrabble('beegeek', 'beegeek'))