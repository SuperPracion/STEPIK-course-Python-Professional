letters = list(map(lambda x: 1040 <= x <= 1103,[ord(input()) for _ in range(3)]))

if all(letters):
    print('ru')
elif any(letters):
    print('mix')
else:
    print('en')
