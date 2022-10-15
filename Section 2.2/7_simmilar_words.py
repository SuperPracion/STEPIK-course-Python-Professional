vowels = 'ауоыиэяюёе'
consonants = 'бвгджзйклмнпрстфхцчшщьъ'

main_word = ''.join(map(lambda x: '1' if x in vowels else '0', input()))
n = int(input())

for _ in range(n):
    challenger = input()
    broken_word = ''.join(map(lambda x: '1' if x in vowels else '0', challenger))
    if main_word[:main_word.rindex('1') + 1] in broken_word[:challenger.rindex('1') + 1]:
        print(challenger)