from datetime import *

def fill_up_missing_dates(dates):
    dates = [datetime.strptime(day, '%d.%m.%Y') for day in dates]
    full_dates = []

    for day in range(min(dates).toordinal(), max(dates).toordinal() + 1):
        full_dates.append(datetime.fromordinal(day).strftime('%d.%m.%Y'))

    return full_dates

