import json

with open('people.json', 'r', encoding='utf-8') as file, open('updated_people.json', 'w', encoding='utf-8') as new_file:
    data = json.load(file)
    shared_keys = set()

    for line in data:
        shared_keys.update(list(line.keys()))

    for line in data:
        for key in shared_keys:
            if key not in line:
                line[key] = None

    json.dump(data, new_file, indent=3)