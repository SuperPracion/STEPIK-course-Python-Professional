import sys
import re

# count = 0
# for line in sys.stdin:
#     if re.search(r'beegeek', line, re.IGNORECASE):
#         count += 1

print(sum([1 for line in sys.stdin if re.search(r'beegeek', line, re.IGNORECASE)]))