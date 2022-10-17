from datetime import *

date_min = min([date.fromisoformat(input()) for _ in range(2)])
print(date_min.strftime('%d-%m (%Y)'))