import re
import sys

pattern = r'^(\w+)\1$'

for line in sys.stdin:
    if re.search(pattern, line):
        print(line, end='')