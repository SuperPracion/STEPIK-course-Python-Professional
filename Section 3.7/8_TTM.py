import calendar
import datetime

year = int(input())

for month in range(1, 13):
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        if datetime.date(year, month, day).weekday() == 3:
            print(datetime.date(year, month, day + 14).strftime('%Y.%m.%d'))
            break
