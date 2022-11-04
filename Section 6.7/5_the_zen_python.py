from collections import *

with open('pythonzen.txt', 'r', encoding='utf-8') as file:
    counter = Counter([letter.lower() for letter in file.read() if letter.isalpha()])

for alpha, value in sorted(counter.items()):
    print(f'{alpha}: {value}')