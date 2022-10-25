import csv

with open('titanic.csv', 'r', encoding='utf-8') as file:
    mens = []
    women = []
    for survived, name, sex, age in list(csv.reader(file, delimiter=';'))[1:]:
        if int(survived) and float(age) < 18:
            if sex == 'male':
                mens.append(name)
            else:
                women.append(name)

    print(*mens, *women, sep='\n')