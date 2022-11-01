from  collections import *

Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])

print(Fruit._fields)