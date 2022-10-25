import csv

with open('deniro.csv', 'r', encoding='utf-8') as file:
    row = int(input()) - 1
    data = sorted(csv.reader(file), key=lambda x: int(x[row]) if (x[row]).isdigit() else x[row])

    for line in data:
        print(*line, sep=',')