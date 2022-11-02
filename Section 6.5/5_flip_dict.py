from collections import *

def flip_dict(dict_of_lists):
    result = defaultdict(list)

    for key, values in dict_of_lists.items():
        for value in values:
            result[value].append(key)

    return result


data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}

for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')