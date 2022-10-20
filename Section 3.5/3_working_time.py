from datetime import *

working_time = [('9:00', '21:00'),
                ('9:00', '21:00'),
                ('9:00', '21:00'),
                ('9:00', '21:00'),
                ('9:00', '21:00'),
                ('10:00', '18:00'),
                ('10:00', '18:00')]

current_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
current_time = current_date.time()

start, end = [datetime.strptime(x, '%H:%M') for x in working_time[current_date.weekday()]]

if current_time < start.time() or current_time >= end.time():
    print('Магазин не работает')
else:
    hours, minutes, seconds = [int(i) for i in str(end - current_date).split(',')[1].split(':')]
    print(int(timedelta(hours=hours, minutes=minutes).total_seconds() // 60))
