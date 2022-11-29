def primes(left, right):
    left = left if left != 1 else 2

    for num in range(left, right + 1):
        if not any([num % i == 0 for i in range(2, num)]):
            yield num


generator = primes(1, 15)

print(*generator)