from datetime import date

def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start

    return sum([date.fromordinal(days).weekday() == 5 for days in range(start.toordinal(), end.toordinal() + 1)])