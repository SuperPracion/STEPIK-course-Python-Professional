def polynom(x):
    polynom.__dict__.setdefault('values', set())

    res = (x**2) + 1
    polynom.values.add(res)

    return res
