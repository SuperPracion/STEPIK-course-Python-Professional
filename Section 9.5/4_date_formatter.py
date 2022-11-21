from datetime import *


def date_formatter(country_code):
    format = {'ru': '%d.%m.%Y',
              'us': '%m-%d-%Y',
              'ca': '%Y-%m-%d',
              'br': '%d/%m/%Y',
              'fr': '%d.%m.%Y',
              'pt': '%d-%m-%Y'}

    return lambda x: x.strftime(format[country_code])


date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))
