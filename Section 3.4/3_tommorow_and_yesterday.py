from datetime import *

today = datetime.strptime(input(), '%d.%m.%Y')

print(date.strftime(today - timedelta(days=1), '%d.%m.%Y'))
print(date.strftime(today + timedelta(days=1), '%d.%m.%Y'))