import json
import csv

with open('students.json', 'r', encoding='utf-8') as file:
    students = json.load(file)
    selection = []

    for student in students:
        if student['age'] >= 18 and student['progress'] >= 75:
            selection.append([student['name'], student['phone']])

    selection.sort()

with open('data.csv', 'w', encoding='utf-8') as selection_students:
    file_writer = csv.writer(selection_students)
    file_writer.writerow(['name', 'phone'])
    file_writer.writerows(selection)
