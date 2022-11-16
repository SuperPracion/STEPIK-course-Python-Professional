def my_pow(number):
    return [int(i) ** degree + 1 for degree, i in enumerate(str(number))]