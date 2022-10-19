from datetime import *

start_date = datetime.strptime(input(), '%d.%m.%Y')
step = timedelta(days=1)

for _ in range(10):
    print(start_date.strftime('%d.%m.%Y'))
    step += timedelta(days=1)
    start_date += step
