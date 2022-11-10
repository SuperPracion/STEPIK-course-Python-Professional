numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

remainders = []

for number in numbers:
    if number != 0:
        remainders.append(36 % number)

print(remainders)