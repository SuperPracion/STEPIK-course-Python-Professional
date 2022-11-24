import functools

@functools.cache
def ways(n):
    if n == 1:
        return 1
    elif n < 1:
        return 0
    else:
        return ways(n - 1) + ways(n - 3) + ways(n - 4)

print(ways(2))