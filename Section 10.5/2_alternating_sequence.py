def alternating_sequence(count=None):
    num = 0
    while num != count:
        num += 1
        yield [-num, num][num % 2]


generator = alternating_sequence(10)

print(*generator)