import datetime

def years_days(year):
    start_date = datetime.date(year=year, month=1, day=1)

    while start_date.year == year:
        yield start_date
        start_date += datetime.timedelta(1)
