import re
import sys

text = sys.stdin.read()
pattern = '''<\w+(?=\s|>)(?:[^>=]|='[^']*'|="[^"]*"|=[^'"][^\s>]*)*?>'''
tags = {}

for line in re.findall(pattern, text):
    tag = ''.join(re.findall('<[a-z]+', line)).replace('<', '')

    for str in re.findall('[a-z]+=', line):
        tags[tag] = tags.get(tag, set()).add(''.join(str.replace('=', '')))

for tag in sorted(tags):
    print(f'{tag}: {sorted(list(set(tags[tag])))}')



# [a-z]+= для поиска элементов
# <[a-z]+ ? для поиска тегов?