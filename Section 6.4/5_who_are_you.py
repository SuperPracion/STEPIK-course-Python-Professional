import datetime
import csv
from collections import *

def comp_sort_by_datetime(friend):
    data = datetime.datetime.strptime(friend.meeting_date, '%d.%m.%Y')
    time = datetime.datetime.strptime(friend.meeting_time, '%H:%M')
    return data, time

Friend = namedtuple('Friend', ['surname', 'name', 'meeting_date', 'meeting_time'])
friends = []


with open('meetings.csv', 'r', encoding='utf-8') as file:
    for friend in list(csv.DictReader(file)):
        friends.append(Friend._make(friend.values()))

for friend in sorted(friends, key=lambda x: comp_sort_by_datetime(x)):
    print(f'{friend.surname} {friend.name}')

