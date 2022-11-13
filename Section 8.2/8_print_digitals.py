def print_digits(numbers):
    if numbers:
        print(numbers % 10)
        print_digits(numbers // 10)