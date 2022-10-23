import sys

height = list(map(int, sys.stdin))

if height:
    print(f'Рост самого низкого ученика: {min(height)}')
    print(f'Рост самого высокого ученика: {max(height)}')
    print(f'Средний рост: {sum(height) / len(height)}')
else:
    print('нет учеников')