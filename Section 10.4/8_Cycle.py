class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iter = iter(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iter)
        except:
            self.iter = iter(self.iterable)
            return next(self.iter)


cycle = Cycle([1])

print(next(cycle) + next(cycle) + next(cycle))