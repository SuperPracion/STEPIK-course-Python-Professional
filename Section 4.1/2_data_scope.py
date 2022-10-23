import datetime
import sys

dates = [datetime.datetime.strptime(in_date.strip(), '%d.%m.%Y') for in_date in sys.stdin]

if dates == sorted(set(dates)):
    print('ASC')
elif dates == sorted(set(dates), reverse=True):
    print('DESC')
else:
    print('MIX')