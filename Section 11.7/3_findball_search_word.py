import re

text = input()
word = input()

print(len(re.findall(fr'\b{word}\b', text)))