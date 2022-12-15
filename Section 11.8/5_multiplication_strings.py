import re


def multiplication_str(match_obj):
    mult, string = match_obj.group(1, 2)
    return string * int(mult)


text = input()

while re.search(r'(\d+)\((\w+?)\)', text):
    text = re.sub(r'(\d+)\((\w+?)\)', multiplication_str, text)

print(text)


