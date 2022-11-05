from collections import *
from sys import stdin

exam_result = Counter()

for data in list(stdin):
    key, value = data.split()
    exam_result[key] = int(value)

print(exam_result.most_common()[-2][0])