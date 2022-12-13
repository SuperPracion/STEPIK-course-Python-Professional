import re

patters = r'Здравствуйте|Доброе утро|Добрый день|Добрый вечер'

if re.match(patters, input(), re.IGNORECASE):
    print(True)
else:
    print(False)