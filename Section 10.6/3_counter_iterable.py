def count_iterable(iterable) -> int:
    return sum(1 for _ in iterable)

print(count_iterable([1, 2, 3, 4, 5]))