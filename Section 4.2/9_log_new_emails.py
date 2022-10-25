import csv

with open('name_log.csv', 'r', encoding='utf-8') as file, open('new_name_log.csv', 'w', encoding='utf-8') as out_log:
    header, *rows = csv.reader(file)
    data = {i[1]:i for i in sorted(rows, key=lambda x: x[2])}

    writer = csv.writer(out_log)
    writer.writerow(header)
    writer.writerows(sorted(data.values(), key=lambda x: x[1]))

