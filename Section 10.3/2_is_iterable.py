def is_iterable(obj):
    try:
        obj.__iter__()
        return True
    except:
        return False

objects = [(1, 13), 7.0004, [1, 2, 3]]

for obj in objects:
    print(is_iterable(obj))