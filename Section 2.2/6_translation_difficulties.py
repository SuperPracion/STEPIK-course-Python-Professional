n = int(input())
common_language = set(input().split(', '))

for _ in range(n - 1):
    common_language &= set(input().split(', '))

if common_language:
    print(*sorted(common_language), sep=', ')
else:
    print('Сериал снять не удастся')