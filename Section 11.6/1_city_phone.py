import re
import sys

pattern = r'(?P<country>\d*)[- ]?(?P<city>\d*)[- ]?(?P<number>\d*)'

for line in sys.stdin:
    match = re.search(pattern, line)
    print(f'Код страны: {match.group("country")}, '
          f'Код города: {match.group("city")}, '
          f'Номер: {match.group("number")}')