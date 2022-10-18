from datetime import *

busy_dates = set()


def formaton_dates_in_mass(date):
    mass_dates = set()

    if '-' in date:
        start_date, end_date = [int(datetime.timestamp(datetime.strptime(day, '%d.%m.%Y'))) for day in date.split('-')]

        for day in range(start_date, end_date + 1):
            mass_dates.add(datetime.fromtimestamp(day).date())

    else:
        mass_dates.add(datetime.strptime(date, '%d.%m.%Y').date())

    return mass_dates


def is_available_date(dates, some_date):
    for date_in_dates in dates:
        for correct_date in formaton_dates_in_mass(date_in_dates):
            busy_dates.add(correct_date)

    return  all(map(lambda x: x not in busy_dates, formaton_dates_in_mass(some_date)))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))
