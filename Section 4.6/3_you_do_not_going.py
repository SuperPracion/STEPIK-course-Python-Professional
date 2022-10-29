import pickle

def filter_dump(filename, objects, typename):
    with open(filename, 'wb') as file:
        req_values = [obj for obj in objects if type(obj) == typename]
        pickle.dump(req_values, file)

filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)