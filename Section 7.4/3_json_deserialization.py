from json import *

try:
    file_name = input()
    with open(file_name, 'r', encoding='utf-8') as file:
        print(load(file))

except ValueError:
    print('Ошибка при десериализации')
except FileNotFoundError:
    print('Файл не найден')