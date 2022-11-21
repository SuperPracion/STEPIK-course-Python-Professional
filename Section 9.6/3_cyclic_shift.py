def cyclic_shift(numbers: list[int | float], step: int) -> None:
    l_mass = len(numbers)
    numbers[:] = [numbers[(i - step) % l_mass] for i in range(l_mass)]

numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)

print(numbers)