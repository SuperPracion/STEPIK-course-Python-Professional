from datetime import *

some_date = datetime.strptime(input(), '%d.%m.%Y')
need_dates = [(some_date + timedelta(days=i)).date() for i in range(1, 8)]
coworkers = {}
birthdays_soon = {}

for _ in range(int(input())):
    name, last_name, some_birthday = input().split(' ')
    day, month, year = [int(i) for i in some_birthday.split('.')]

    coworkers[f'{name} {last_name}'] = date(year, month, day)

for coworker in coworkers:
    for date in need_dates:
        if coworkers[coworker].month == date.month and coworkers[coworker].day == date.day:
            birthdays_soon[coworker] = coworkers[coworker]

if birthdays_soon:
    print(sorted(birthdays_soon, key=coworkers.get)[0])
else:
    print('Дни рождения не планируются')