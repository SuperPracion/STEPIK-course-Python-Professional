from sys import *

sum_numbers = 0
counter_not_nums = 0

for element in stdin:
    try:
        sum_numbers += int(element)
    except ValueError:
        try:
            sum_numbers += float(element)
        except:
            counter_not_nums += 1

print(sum_numbers)
print(counter_not_nums)
