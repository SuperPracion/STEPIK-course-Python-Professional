import csv


def key_sort(grade):
    nums, alpha = grade.split('-')
    return int(nums), alpha


with open('student_counts.csv', 'r', encoding='utf-8') as file, open('sorted_student_counts.csv', 'w', encoding='utf-8') as output:
    header = list(csv.DictReader(file))
    sorted_class = ['year'] + sorted(list(header[0].keys())[1:], key=key_sort)

    writer = csv.writer(output)
    writer.writerow(sorted_class)

    for data in sorted(header, key=lambda x: x['year']):
        temp = [data['year']]
        for order in sorted_class:
            temp.append(data[order])
        writer.writerow(temp)
