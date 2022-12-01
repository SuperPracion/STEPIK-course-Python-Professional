def with_previous(iterable, previous=None):
    for iter in iterable:
        yield (iter, previous)
        previous = iter

iterator = iter('stepik')

print(*with_previous(iterator))