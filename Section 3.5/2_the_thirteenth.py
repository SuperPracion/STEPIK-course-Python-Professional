from datetime import *

day = date(day=1, month=1, year=1)
weekdays = [0, 0, 0, 0, 0, 0, 0]

while day != date(day=31, month=12, year=9999):
    if day.day == 13:
        weekdays[day.weekday()] += 1

    day += timedelta(days=1)

print(*weekdays, sep='\n')