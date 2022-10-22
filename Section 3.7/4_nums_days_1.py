import calendar
import datetime

dt = datetime.datetime.strptime(input(), '%Y %m')
print(calendar.monthrange(dt.year, dt.month)[1])