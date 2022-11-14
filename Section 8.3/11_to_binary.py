def to_binary(number):
    if number in (1, 0):
        return str(number)
    else:
        return str(to_binary(number // 2)) + str(number % 2)
