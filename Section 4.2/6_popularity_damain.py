import csv

with open('domain_usage.csv', 'w', encoding='utf-8') as output, open('data.csv', 'r', encoding='utf-8') as file:
    rows = list(csv.reader(file))
    domains = {}
    for email in list(zip(*rows))[2][1:]:
        domain = email.split('@')[1]
        domains[domain] = domains.get(domain, 0) + 1

    output.write('domain,count\n')
    for row in sorted(sorted(domains.keys()), key=lambda x: domains[x]):
        output.write(f'{row},{domains[row]}\n')