import json
import sys

for key, value in json.load(sys.stdin).items():
    if type(value) == list:
        print(f'{key}: {", ".join(map(str, value))}')
    else:
        print(f'{key}: {value}')