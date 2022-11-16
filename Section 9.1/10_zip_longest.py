def zip_longest(*args, fill=None):
    max_len_list = max(map(len, args))
    lists = [i + [fill] * (max_len_list - len(i)) for i in args]

    return list(zip(*lists))

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))