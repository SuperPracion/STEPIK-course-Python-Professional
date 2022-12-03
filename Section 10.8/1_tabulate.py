import itertools

def tabulate(func):
    for i in itertools.count(1):
        yield func(i)

func = lambda x: x + 10
values = tabulate(func)

print(next(values))
print(next(values))
print(next(values))