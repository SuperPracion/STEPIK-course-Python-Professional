import sys

mass_nums = list(map(int, sys.stdin))
if len(mass_nums) % 2 == 1:
    if mass_nums[-1] % 2 == 0:
        print('Дима')
    else:
        print('Анри')
else:
    if mass_nums[-1] % 2 == 0:
        print('Анри')
    else:
        print('Дима')
