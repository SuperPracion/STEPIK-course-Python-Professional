from datetime import *

def get_date_range(start, end):
    range_dates = [date.fromordinal(days) for days in range(start.toordinal(), end.toordinal() + 1)]

    return range_dates

date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)

print(get_date_range(date1, date2))