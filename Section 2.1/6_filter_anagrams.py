def filter_anagrams(word, words):
    return [string for string in words if sorted(word) == sorted(string)]

print(filter_anagrams('стекло', []))