from datetime import *

start_day = datetime.strptime(input(), '%H:%M')
end_day = datetime.strptime(input(), '%H:%M')

while start_day + timedelta(minutes=55) <= end_day:
    print(start_day.strftime('%H:%M'), (start_day + timedelta(minutes=45)).strftime('%H:%M'))
    start_day += timedelta(minutes=55)
