import re

word = input()
text = input()

print(len(re.findall(fr'\b{word[:-2]}(se|ze)\b', text, re.IGNORECASE)))