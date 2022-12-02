def pairwise(iterable):
    iterable = iter(iterable)
    try:
        back = next(iterable)
        for i in iterable:
            yield back, i
            back = i
        else:
            yield back, None
    except:
        pass



numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))