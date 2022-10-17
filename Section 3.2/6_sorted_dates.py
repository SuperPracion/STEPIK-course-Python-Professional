from datetime import *

dates = [date.fromisoformat(input()) for _ in range(int(input()))]

for date in sorted(dates):
    print(date.strftime('%d/%m/%Y'))