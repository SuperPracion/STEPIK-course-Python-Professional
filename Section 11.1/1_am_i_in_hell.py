from re import *

in_str = input()
print(*findall(r'7-\d{3}-\d{3}-\d{2}-\d{2}|8-\d{3}-\d{4}-\d{4}', in_str), sep='\n')

# |8-\d{3}-\d{4}-\d{3}