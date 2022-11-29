def flatten(nested_list):
    for some in nested_list:
        yield from flatten(some) if isinstance(some, list) else [some]

generator = flatten([1, 2, 3, 4, 5, 6, 7])

print(*generator)