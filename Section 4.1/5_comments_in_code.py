# put your python code here
import sys

strings = list(map(str.strip, sys.stdin))
print(len([filter(lambda x: x[0] == '#', strings)]))
