from datetime import *
coworkers = {}
n = int(input())

for _ in range(n):
    name, last_name, some_date = input().split(' ')
    day, month, year = some_date.split('.')

    coworkers[date(day=int(day), month=int(month), year=int(year))] = f'{name} {last_name}'

max_old = min(coworkers.keys())

if len(coworkers) != n:
    print(max_old.strftime('%d.%m.%Y'), n - (len(coworkers) - 1))
else:
    print(max_old.strftime('%d.%m.%Y'), coworkers[max_old])