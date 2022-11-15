def linear(nested_lists):
    mass = []

    for element in nested_lists:
        if type(element) != list:
            mass.append(element)
        else:
            mass += linear(element)

    return mass

my_list = [10, 20, 30, 40, 50]

print(linear(my_list))