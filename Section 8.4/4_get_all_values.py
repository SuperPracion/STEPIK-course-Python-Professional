def get_all_values(nested_dicts, key, out_set=()):
    out_set = set()

    for k, v in nested_dicts.items():
        if key in nested_dicts:
            out_set.add(nested_dicts[key])
        if type(v) == dict:
            out_set.update(get_all_values(v, key))

    return out_set

my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))