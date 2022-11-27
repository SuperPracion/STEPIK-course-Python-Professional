import random


def random_numbers(left, right):
    return iter(lambda: random.randint(left, right + 1), '')


iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))
