def get_min_max(iterable):
    try:
        max = min = next(iter(iterable))
        for num in iterable:
            if num > max:
                max = num
            if num < min:
                min = num

        return min, max
    except:
        return None

data = iter(range(100_000_000))

print(get_min_max(data))