from json import *
from collections import *

with open('zoo.json', 'rt', encoding='utf-8') as file:
    animals = ChainMap(*load(file))
    print(sum(animals.values()))