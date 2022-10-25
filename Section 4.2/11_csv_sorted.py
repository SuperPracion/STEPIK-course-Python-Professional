import csv

def condense_csv(filename, id_name):
    with open(filename, 'r', encoding='utf-8') as file, open('condensed.csv', 'w', encoding='utf-8') as output:
        objects = {}
        for obj, attr, value in csv.reader(file):
            if obj not in objects:
                objects[obj] = {id_name: obj}
            objects[obj][attr] = value


        writer = csv.DictWriter(output, fieldnames=objects[obj])
        writer.writeheader()
        writer.writerows(objects.values())

condense_csv('test.csv', 'ID')
