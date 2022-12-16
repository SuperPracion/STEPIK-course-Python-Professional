import re


def multiple_split(string, delimiters):
    split_string = '|'.join(map(re.escape, sorted(delimiters, reverse=True)))
    return re.split(fr'{split_string}', string)

print(multiple_split('beegeek-python.stepik', ['.', '-']))
print(multiple_split('Timur---Arthur+++Dima****Anri', ['---', '+++', '****']))
print(multiple_split('timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan', ['.^[+']))