import json

with open('data.json', 'r', encoding='utf-8') as file, open('updated_data.json', 'w', encoding='utf-8') as output:
    data = json.load(file)
    update_data = []

    for item in data:
        match item:
            case str():
                update_data.append(item + '!')
            case bool():
                update_data.append(not item)
            case int():
                update_data.append(item + 1)
            case dict():
                item["newkey"] = None
                update_data.append(item)
            case list():
                update_data.append(item * 2)
            case _:
                continue

    json.dump(update_data, output, indent=3)
