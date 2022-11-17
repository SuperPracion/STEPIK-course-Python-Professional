def hash_as_key(objects):
    hash_elements = {}

    for obj in objects:
        h_obj = hash(obj)

        if h_obj in hash_elements:
            values = hash_elements[h_obj]

            if type(values) != list:
                values = [values]

            hash_elements[h_obj] = values + [obj]
        else:
            hash_elements[h_obj] = obj

    return hash_elements


data = [-1, -2, -3, -4, -5]

print(hash_as_key(data))
