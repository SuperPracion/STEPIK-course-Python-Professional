import json
from datetime import datetime


def sort_by_length_wight(dimensions):
    length, width = dimensions['Length'], dimensions['Width']
    return int(length), int(width)


with open('pools.json', 'r', encoding='utf-8') as file:
    pools = json.load(file)

    for pool in sorted(pools, key=lambda x: sort_by_length_wight(x['DimensionsSummer']), reverse=True):
        opened, closed = (pool['WorkingHoursSummer']['Понедельник']).split('-')

        if (datetime.strptime(opened, '%H:%M') <= datetime.strptime("10:00", '%H:%M') and
            datetime.strptime(closed, '%H:%M') >= datetime.strptime("12:00", '%H:%M')):

            print(f'{pool["DimensionsSummer"]["Length"]}x{pool["DimensionsSummer"]["Width"]}\n{pool["Address"]}')
            break