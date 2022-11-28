class PowerOf:
    def __init__(self, n):
        self.n = n
        self.pow = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.n ** self.pow
        self.pow += 1

        return value
