import csv

with open('grades.csv', encoding='utf-8') as csv_file:
    text = csv_file.readlines()
    rows = csv.reader(text, delimiter=';')
    for row in rows:
        print(row)