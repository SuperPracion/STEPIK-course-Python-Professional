def around(iterable):
    iterable = iter(iterable)
    try:
        back, current = None, next(iterable)
        for i in iterable:
            yield back, current, i
            back, current = current, i
        else:
            yield back, current, None
    except:
        pass

iterator = iter('hey')

print(*around(iterator))