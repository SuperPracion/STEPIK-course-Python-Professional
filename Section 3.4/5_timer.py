from datetime import *

timer_time = datetime.strptime(input(), '%H:%M:%S')
timer = timedelta(seconds=int(input()))

print((timer_time + timer))