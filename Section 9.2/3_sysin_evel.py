import sys

res = [eval(expression.strip()) for expression in sys.stdin]
print(max(res))