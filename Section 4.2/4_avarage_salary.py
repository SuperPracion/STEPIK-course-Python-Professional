import csv

with open('salary_data.csv', 'r', encoding='utf-8') as file:
    com_and_sal = {}
    rows = list(csv.reader(file, delimiter=';'))

    for company, salary in rows[1:]:
        com_and_sal[company] = com_and_sal.get(company, list()) + list([int(salary)])

    print(*sorted(com_and_sal.keys(), key=lambda x: sum(com_and_sal[x]) / len(com_and_sal[x])), sep='\n')
