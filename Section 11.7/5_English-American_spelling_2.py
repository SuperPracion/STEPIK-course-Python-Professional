import re

word = input()
text = input()

print(len(re.findall(fr'\b{word[:-3]}(or|our)\b', text, re.IGNORECASE)))