import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
week = {num + 1: day.title() for num, day in enumerate(calendar.day_name)}


def get_weekday(day):
    if not type(day) == int:
        raise TypeError('Аргумент не является целым числом')

    if not 1 < day < 8:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')

    return week[day]

