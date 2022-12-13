import re
import sys

count = 0
for line in sys.stdin:
    if re.search(r'^beegeek.*beegeek$', line):
        count += 3
    elif re.search(r'^beegeek.*|.*beegeek$', line):
        count += 2
    elif re.search(r'.*beegeek', line):
        count += 1

print(count)