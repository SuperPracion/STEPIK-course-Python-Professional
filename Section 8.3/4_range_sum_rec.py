def range_sum(numbers, start, end):
    if start > end:
        return 0
    else:
        return numbers[start] + range_sum(numbers, start + 1, end)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))
