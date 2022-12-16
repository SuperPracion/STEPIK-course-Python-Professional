import re

start, end = map(int, input().split())
regex_obj = re.compile('\d+')

nums = regex_obj.findall(input(), pos=start, endpos=end)

print(sum(map(int, nums)))
