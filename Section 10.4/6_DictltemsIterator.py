class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.keys = iter(data)

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.keys)

        return (key, self.data[key])

data = {'Arthur': 100, 'Timur': 100, 'Dima': 100,
        'Anri': 101, 'Roma': 99, 'German': 98}

pairs = DictItemsIterator(data)

print(list(pairs))