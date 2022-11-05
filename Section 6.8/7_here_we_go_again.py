from collections import *

with open('name_log.csv', 'r', encoding='utf-8') as file:
    data = file.readlines()[1:]
    emails = Counter(info.split(',')[1] for info in data)

for email,value in sorted(emails.items()):
    print(f'{email}: {value}')