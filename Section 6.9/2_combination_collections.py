from collections import *

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}


prices = ChainMap(bread, meat, sauce, vegetables, toppings)
need_products = Counter(input().split(','))
max_pos_len = max(map(len, need_products))

total = 0
len_strings = []

for pos, quantity in sorted(need_products.items()):
    total += prices[pos] * quantity
    temp_str = f'{pos}{"".ljust(max_pos_len - len(pos))} x {quantity}'

    len_strings.append(len(temp_str))
    print(temp_str)

summery = f'ИТОГ: {total}р'
len_strings.append(len(summery))

print('-' * max(len_strings))
print(summery)