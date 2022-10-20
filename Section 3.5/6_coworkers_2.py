from datetime import *
n = int(input())
birthdays = {}

for _ in range(n):
    name, last_name, some_date = input().split(' ')
    day, month, year = [int(i) for i in some_date.split('.')]

    birthdays[date(year, month, day)] = birthdays.get(date(year, month, day), 0) + 1

for date in sorted(filter(lambda key: birthdays[key] == max(birthdays.values()), birthdays.keys())):
    print(date.strftime('%d.%m.%Y'))