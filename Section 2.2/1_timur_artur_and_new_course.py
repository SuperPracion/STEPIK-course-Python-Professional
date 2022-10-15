nums = sorted([int(input()) for _ in range(3)])
print(min(sum(nums), (min(nums) * 2 + nums[1] * 2)))
