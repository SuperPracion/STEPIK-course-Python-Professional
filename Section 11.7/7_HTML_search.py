import re
import sys

text = sys.stdin.read()
pattern = r'<a href="(.+)">(.+)</a>'

for address, pointer  in re.findall(pattern, text):
    print(f'{address}, {pointer}')