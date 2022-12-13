import re
import sys

counter_for_bee = 0
counter_for_geek = 0

for line in sys.stdin:
    if re.search(r'.*bee.*bee.*', line):
        counter_for_bee += 1

    if re.search(r'\bgeek\b', line):
        counter_for_geek += 1

print(counter_for_bee, counter_for_geek, sep='\n')