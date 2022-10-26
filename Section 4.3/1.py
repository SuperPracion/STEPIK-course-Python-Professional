import json

data = {"name": "Russia", "phone_code": 7, "capital": "Moscow", "currency": "RUB", "square": 17100000}

with open('contries.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, sort_keys=True, separators=(',', ' : '))

# print(json.dumps(data, indent=4, ensure_ascii=False))

# json_data = '{"name": "\u0420\u043e\u0441\u0441\u0438\u044f", "phone_code": 7, "capital": "Moscow", "currency": "RUB", "square": 17100000}'
#
# data = json.loads(json_data)
# print(data)

# with open('contries.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     for key, value in data.items():
#         if type(value) == list:
#             print(f'{key}: {", ".join(value)}')
#         else:
#             print(f'{key}: {value}')