from collections import *


def get_all_values(chainmap, name):
    return set([person[name] for person in chainmap.maps if name in person])


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'age')

print(result)
