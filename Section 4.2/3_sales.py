import csv

with open('sales.csv', 'r', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=';'))
    del rows[0]
    for name, old_price, new_price in rows:
        if int(new_price) < int(old_price):
            print(name)