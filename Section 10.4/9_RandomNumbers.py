import random

class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1

        return random.randint(self.left, self.right)

iterator = RandomNumbers(1, 10, 2)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))