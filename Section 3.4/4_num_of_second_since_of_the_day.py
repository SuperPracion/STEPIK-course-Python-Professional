from datetime import *

hours, minutes, seconds = [int(i) for i in input().split(':')]

time = datetime.strptime(hours=hours, minutes=minutes, seconds=seconds)

print(time.total_seconds())