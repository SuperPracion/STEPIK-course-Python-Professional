class Repeater:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        pass

    def __next__(self):
        return self.obj

geek = Repeater('geek')

print(next(geek))
print(next(geek))
print(next(geek))