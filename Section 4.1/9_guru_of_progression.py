import sys

nums = list(map(int, sys.stdin))

if nums == [nums[0] + (i - 1) * (nums[1] - nums[0])for i in range(1, len(nums) + 1)]:
    print('Арифметическая прогрессия')
elif nums == [nums[0] * (nums[1] - nums[0])**(i - 1)for i in range(1, len(nums) + 1)]:
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')
