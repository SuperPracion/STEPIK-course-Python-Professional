def stop_on(iterable, obj):
    for iter in iterable:
        if iter == obj:
            break
        yield iter

iterator = iter('beegeek')

print(*stop_on(iterator, 'a'))