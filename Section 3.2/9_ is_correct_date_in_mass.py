from datetime import *


def is_correct(day, month, year):
    is_correct_flag = True

    try:
        date(year, month, day)
    except:
        is_correct_flag = False

    return is_correct_flag


count_correct_date = 0
some_date = input()

while some_date != 'end':
    if is_correct(*map(int, some_date.split('.'))):
        print('Корректная')
        count_correct_date += 1
    else:
        print('Некорректная')

    some_date = input()

print(count_correct_date)
