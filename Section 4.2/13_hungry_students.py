import csv

def key_comparator(gride):
    _, price, n_shop = gride[0], gride[1][0], gride[1][1]
    return int(price), sum(map(ord, n_shop))

with open('prices.csv', 'r', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=';'))

    data = {}
    for info in reader:
        shop = info.pop('Магазин')
        for product in info:
            data[product] = data.get(product, [info[product], shop])

            if int(info[product]) <= int(data[product][0]):
                data[product] = [info[product], shop]

    n_product, info = min(data.items(), key=key_comparator)
    print(f'{n_product.title()}: {info[1]}')




