def sort_priority(values, group):
    return values.sort(key=lambda x: (x not in group, x))


numbers = [150, 200, 300, 1000, 50, 20000]
sort_priority(numbers, [300, 100, 200])

print(numbers)