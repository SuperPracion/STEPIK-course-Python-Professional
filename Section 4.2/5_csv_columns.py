import csv

def csv_columns(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        rows = list(csv.reader(file))
        return ({key: value for key, *value in list(zip(*rows))})
