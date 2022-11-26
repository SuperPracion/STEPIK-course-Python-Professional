def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool

    return filter(lambda elem: not predicate(elem), iterable)


objects = [0, 1, True, False, 17, []]

print(*filterfalse(None, objects))
