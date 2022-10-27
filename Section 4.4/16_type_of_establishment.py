import json

with open('food_services.json', 'r', encoding='utf-8') as file:
    restaurants = json.load(file)
    need_objects = {}

    for restaurant in restaurants:
        type_object, name, seats_count = restaurant['TypeObject'], restaurant['Name'], restaurant['SeatsCount']
        if need_objects.setdefault(type_object, {}).setdefault(name, seats_count) < seats_count:
            need_objects[type_object][name] = seats_count

    for type_obj in sorted(need_objects.keys()):
        name, seats_count = max(need_objects[type_obj].items(), key=lambda x: x[1])
        print(f'{type_obj}: {name}, {seats_count}')