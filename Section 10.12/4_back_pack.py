from collections import namedtuple
from itertools import *

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

back_pack = set()
tonnage = int(input())

for quantity_items in range(1, 11):
    for tpl in combinations(items, r=quantity_items):
        if sum([item.mass for item in tpl]) <= tonnage:
            back_pack.add(tpl)

if not back_pack:
    print('Рюкзак собрать не удастся')
else:
    max_price_for_backpack = max(back_pack, key=lambda cargo: sum([item.price for item in cargo]))

    for item in sorted(max_price_for_backpack, key=lambda item: item.name):
        print(item.name)