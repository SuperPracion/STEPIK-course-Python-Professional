from datetime import *

f_date = datetime.strptime(input(), '%d.%m.%Y').date()
s_date = datetime.strptime(input(), '%d.%m.%Y').date()

while (f_date.day + f_date.month) % 2 != 1:
    f_date += timedelta(days=1)

while f_date <= s_date:
    if f_date.weekday() not in [0, 3]:
        print(f_date.strftime('%d.%m.%Y'))

    f_date += timedelta(days=3)