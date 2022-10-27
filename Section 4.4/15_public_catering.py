import json

with open('food_services.json', 'r', encoding='utf-8') as file:
    restaurants = json.load(file)
    rest_in_district = {}
    popularity_rest = {}

    for restaurant in restaurants:
        district, is_net_object, operating_company, = restaurant['District'], restaurant['IsNetObject'], restaurant['OperatingCompany']

        rest_in_district[district] = rest_in_district.get(district, 0) + 1  #счёт ресторанов на цлице

        if is_net_object == 'да': #счёт сети ресторанов
            popularity_rest[operating_company] = popularity_rest.get(operating_company, 0) + 1

    print(*max(rest_in_district.items(), key=lambda x: x[1]), sep=': ')
    print(*max(popularity_rest.items(), key=lambda x: x[1]), sep=': ')


