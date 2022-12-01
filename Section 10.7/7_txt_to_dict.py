def txt_to_dict():
    with open('planets.txt', 'r', encoding='utf-8') as file:
        planets_info = (info.split('\n') for info in file.read().split('\n\n'))
        for planet in planets_info:
            yield {info.split(' = ')[0]: info.split(' = ')[1] for info in planet}

planets = txt_to_dict()

print(next(planets))
