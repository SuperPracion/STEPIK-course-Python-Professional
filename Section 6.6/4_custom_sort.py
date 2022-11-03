from collections import *

def custom_sort(ordered_dict, by_values=False):
    if by_values:
        for key in sorted(ordered_dict.items(), key=lambda x: x[1]):
            ordered_dict.move_to_end(key[0])
    else:
        for key in sorted(ordered_dict.keys()):
            ordered_dict.move_to_end(key)


data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)

print(*data.items())