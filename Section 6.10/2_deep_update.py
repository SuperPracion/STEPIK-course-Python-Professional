from collections import *

def deep_update(chainmap, key, value):
    for data in chainmap.maps:
        if key in data:
            data[key] = value

    chainmap.setdefault(key, value)

    return None

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'age', 20)

print(chainmap)