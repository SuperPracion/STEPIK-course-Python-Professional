def recursive_sum(nested_lists):
    sum = 0

    for element in nested_lists:
        if type(element) == int:
            sum += element
        if type(element) == list:
            sum += recursive_sum(element)

    return sum

my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))
