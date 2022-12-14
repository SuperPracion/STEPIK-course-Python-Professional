import re

text = input()
sub_word = input()

print(len(re.findall(fr'\B{sub_word}\B', text)))