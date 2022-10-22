from calendar import *
from datetime import *

def get_all_mondays(year):
    all_mondays = []
    for month in range(1, 13):
        for day in range(1, monthrange(year, month)[1] + 1):
            if date(year, month, day).weekday() == 0:
                all_mondays.append(date(year, month, day))

    return all_mondays

print(get_all_mondays(2021))