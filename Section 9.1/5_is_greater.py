def is_greater(lists, number):
    return any(sum(list) > number for list in lists)