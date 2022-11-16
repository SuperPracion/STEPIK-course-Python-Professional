def custom_isinstance(objects, typeinfo):
    return sum(isinstance(object, typeinfo) for object in objects)

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, int))