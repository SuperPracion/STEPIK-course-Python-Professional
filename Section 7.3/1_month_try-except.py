import calendar

months = {num: month for num, month in enumerate(calendar.month_name) if num}

try:
    month = int(input())
    print(months[month])
except KeyError:
    print('Введено число из недопустимого диапазона')
except ValueError:
    print('Введено некорректное значение')