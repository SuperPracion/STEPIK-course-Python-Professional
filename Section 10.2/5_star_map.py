def starmap(func, iterable):
    try:
        return list(map(lambda x: func(*x), iterable))
    except:
        return None

points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]

print(*starmap(lambda x, y, z: x * y * z, points))