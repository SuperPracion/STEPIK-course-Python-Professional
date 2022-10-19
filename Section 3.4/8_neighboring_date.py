from datetime import *

mass_date = [datetime.strptime(day, '%d.%m.%Y') for day in input().split(' ')]
difference_days = []

for day in range(1, len(mass_date)):
    difference_days.append(abs(mass_date[day] - mass_date[day - 1]).days)

print(difference_days)