import sys

strings = list(sys.stdin)
print(*list(filter(lambda x: x.replace(' ', '')[0] != '#', strings)), sep='', end='')