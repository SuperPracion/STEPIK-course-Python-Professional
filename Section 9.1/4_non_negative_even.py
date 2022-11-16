def non_negative_even(numbers):
    return all(i % 2 == 0 and i >= 0 for i in numbers)