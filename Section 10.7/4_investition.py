import csv

with open('data.csv', 'r', encoding='utf-8') as file:
    data = csv.DictReader(file)
    invest_in_A_round = (info for info in data if info['round'] == 'a')
    res_inv = sum(int(info['raisedAmt']) for info in invest_in_A_round)

    print(res_inv)
