from collections import *

def get_value(chainmap, key, from_left=True):
    if not from_left:
        chainmap.maps.reverse()

    return chainmap.get(key)


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))