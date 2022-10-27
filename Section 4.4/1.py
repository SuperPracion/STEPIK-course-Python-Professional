from datetime import datetime
open, closed = "09:00-12:00".split('-')

print(datetime.strptime(open, '%H:%M') <= datetime.strptime("10:00", '%H:%M') and
      datetime.strptime(closed, '%H:%M') >= datetime.strptime("12:00", '%H:%M'))