def dict_travel(nested_dicts, travel=list()):

    for k, v in sorted(nested_dicts.items()):
        if type(v) == dict:
            dict_travel(v, travel + [k])

        if type(v) != dict:
            print(f'{".".join(travel + [k])}: {v}')




data = {'firstname': 'Тимур',
        'lastname': 'Гуев',
        'birthdate': {'day': 10, 'month': 'October', 'year': 1993},
        'address': {'streetaddress': 'Часовая 25, кв. 127',
                    'city': {'region': 'Московская область', 'type': 'город', 'cityname': 'Москва'},
                    'postalcode': '125315'}}

dict_travel(data)