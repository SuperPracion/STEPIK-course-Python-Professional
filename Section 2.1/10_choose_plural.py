def choose_plural(amount, declensions):
    out_res = f'{amount} {declensions[2]}'

    dict_value = {0: [1, 21, 41, 61, 31, 51, 71, 91],
                  1: [2, 3, 4, 22, 23, 24, 42, 43, 44, 62, 63, 64, 82, 83, 84, 32, 33, 34, 52, 53, 54, 72, 73, 74, 92, 93, 94],}

    for key, value in dict_value.items():
        if amount % 100 in value:
            out_res = f'{amount} {declensions[key]}'

    return out_res

print(choose_plural(111223, ('копейка', 'копейки', 'копеек')))