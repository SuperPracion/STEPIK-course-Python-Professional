import json

with open('countries.json', 'r', encoding='utf-8') as file, open('religion.json', 'w', encoding='utf-8') as new_file:
    data = json.load(file)
    new_data = {}
    for line in data:
        country, religion = line.values()
        new_data[religion] = new_data.get(religion, []) + list([country])

    json.dump(new_data, new_file)