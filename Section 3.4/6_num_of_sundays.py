from datetime import *


def num_of_sundays(year):
    start_date = datetime(year, 1, 1, 1).toordinal()
    end_date = datetime(year + 1, 1, 1).toordinal()

    return sum([1 for day in range(start_date, end_date) if datetime.fromordinal(day).isoweekday() == 7])


print(num_of_sundays(2022))
