from collections import *
from csv import *
from json import *

quarters = ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']


with open('prices.json', 'rt', encoding='utf-8') as file:
    price_list = load(file)


def get_csv_file_price(file_name):
    counter = Counter()

    with open(file_name, 'rt', encoding='utf-8') as file:
        data = list(reader(file))[1:]
        for product, *price in data:
            counter[product] = sum(map(int, price))

    return sum([price_list[product] * amount for product, amount in counter.items()])


total = 0
for i in range(4):
    total += get_csv_file_price(quarters[i])

print(total)
