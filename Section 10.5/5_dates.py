from datetime import *


def dates(start, count=None):
    if count is None:
        count = True

    while count:
        yield start

        if not count is True:
            count -= 1

        try:
            start += timedelta(1)
        except:
            return StopIteration


generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
    print(next(generator))
except StopIteration:
    print('Error')
