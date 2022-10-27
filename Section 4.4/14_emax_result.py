import json
import csv


def comparator_score(params):
    return int(params['score']), params['date_and_time']


with open('exam_results.csv', 'r', encoding='utf-8') as file:
    results = list(csv.DictReader(file))
    final_results = []

    for student in sorted(results, key=lambda x: comparator_score(x)):
        for std_in_final in final_results:
            if student['name'] == std_in_final['name'] and student['surname'] == std_in_final['surname']:
                std_in_final['best_score'] = int(student['score'])
                std_in_final['date_and_time'] = student['date_and_time']
                break
        else:
            final_results.append({'name': student['name'], 'surname': student['surname'], 'best_score': int(student['score']),
                                  'date_and_time': student['date_and_time'], 'email': student['email']})


with open('best_scores.json', 'w', encoding='utf-8') as new_file:
    json.dump(sorted(final_results, key=lambda x: x['email']), new_file, indent=3)
