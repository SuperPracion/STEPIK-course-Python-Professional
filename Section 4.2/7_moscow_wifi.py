import csv

with open('wifi.csv', 'r', encoding='utf-8') as file:
    info = list(csv.reader(file, delimiter=';'))[1:]
    out_dict = {}
    for i in range(len(info)):
        out_dict[info[i][1]] = out_dict.get(info[i][1], 0) + int(info[i][-1])

    for district, number_of_points in sorted(sorted(out_dict.items()), key=lambda x: x[1], reverse=True):
        print(f'{district}: {number_of_points}')
