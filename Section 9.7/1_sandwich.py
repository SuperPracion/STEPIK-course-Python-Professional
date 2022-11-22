def sandwich(func):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        res = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return res

    return wrapper


@sandwich
def beegeek():
    return 'beegeek'


print(beegeek())
