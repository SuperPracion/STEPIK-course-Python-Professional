from datetime import datetime

diary = {}

with open('diary.txt', 'rt', encoding='utf-8') as file:
    content = ''.join(file.readlines()).split('\n\n')

    for line in sorted(content, key=lambda x: datetime.strptime(x[:x.index('\n')], '%d.%m.%Y; %H:%M')):
        print(line, sep='', end='\n\n')





