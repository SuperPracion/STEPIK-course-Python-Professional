from collections import *


def count_occurences(word, words):
    words = Counter(words.lower().split())
    return words[word.lower()]


word = 'Se'
words = 'se sdsf sds SE sdfsdg Se dhgf gfd asd se'

print(count_occurences(word, words))
