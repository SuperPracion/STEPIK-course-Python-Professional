def index_of_nearest(numbers, number):
    if numbers:
        array_difference = list(map(lambda x: abs(x - number), numbers))

        return array_difference.index(min(array_difference))
    else:
        return -1




print(index_of_nearest([7, 5, 4, 4, 3], 4))