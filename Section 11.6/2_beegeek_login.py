import re
import sys

pattern = r'_\d+[a-zA-Z]*_?'

for line in sys.stdin:
    print(bool(re.search(pattern, line)))
