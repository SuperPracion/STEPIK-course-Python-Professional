from collections import *


def print_bar_chart(data, mark):
    data = Counter(data)
    max_len_cell = max(map(len, data.keys()))

    for key, value in data.most_common():
        print(f'{key}{"".ljust(max_len_cell - len(key))} |{mark * value}')

