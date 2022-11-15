def get_value(nested_dicts, key):
    value = nested_dicts.get(key)

    if value is None:
        for k, v in nested_dicts.items():
            if type(v) == dict:
                value = get_value(v, key)
    return value

data = {'first_name': 'Alyson', 'last_name': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

print(get_value(data, 'birthday'))