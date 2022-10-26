import json
import csv

with open('playgrounds.csv', 'r', encoding='utf-8') as file, open('addresses.json', 'w', encoding='utf-8') as new_file:
    addresses = csv.DictReader(file, delimiter=';')
    sort_addresses = {}

    for address in addresses:
        _, AdmArea, District, Address = address.values()
        sort_addresses.setdefault(AdmArea, {}).setdefault(District, []).append(Address)

    json.dump(sort_addresses, new_file, indent=3, ensure_ascii=False)

