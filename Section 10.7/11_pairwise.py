def pairwise(iterable):
    try:
        first = next(iterable)
        for iter in iterable:
            yield first, iter
            first = iter
    except:
        pass



numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))