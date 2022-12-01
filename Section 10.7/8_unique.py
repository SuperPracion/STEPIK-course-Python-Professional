def unique(iterable):
    used_nums = set()
    for i in iterable:
        if i not in used_nums:
            used_nums.add(i)
            yield i



data = map(abs, range(-100, 100))

print(*unique(data))