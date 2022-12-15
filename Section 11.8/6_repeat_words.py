import re

text = input()

while re.search(r'(\b\w+\b)+\W*\1\b', text):
    text = re.sub(r'(\b\w+\b)+\W*(\1\b)', r'\2', text)

print(text)

#(\b\w+\b).{1,2}\1 - для поиска рядом стоящих, одинаковых, слов