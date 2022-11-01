import pickle
from collections import *

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    for animal in pickle.load(file):
        for key, value in zip(Animal._fields, animal):
            print(f'{key}: {value}')

        print()