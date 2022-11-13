def print_digits(numbers):
    if numbers:
        print_digits(numbers // 10)
        print(numbers % 10)