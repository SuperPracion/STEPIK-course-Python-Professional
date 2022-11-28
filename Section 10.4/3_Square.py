class Square:
    def __init__(self, n):
        self.n = n
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 0:
            raise StopIteration
        self.start += 1
        return self.start ** 2
