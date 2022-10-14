def same_parity(numbers):
    # return list(filter(lambda x: x % 2 == numbers[0] % 2, numbers))
    return [i for i in numbers if i % 2 == numbers[0] % 2]

print(same_parity(same_parity([-7, 0, 67, -9, 70, -29, 90])))