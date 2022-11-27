def is_iterator(obj):
    try:
        obj.__next__()
        return True
    except:
        return False


beegeek = map(str.upper, 'beegeek')

print(is_iterator(beegeek))
