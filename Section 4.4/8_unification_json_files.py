import json

with open('data1.json', 'r', encoding='utf-8') as data1, open('data2.json', 'r', encoding='utf-8') as data2, open('data_merge.json', 'w', encoding='utf-8') as new_file:
    dict = json.load(data1) | json.load(data2)
    json.dump(dict, new_file, indent=3)
