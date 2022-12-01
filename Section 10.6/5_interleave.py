def interleave(*args):
    return (elem for arg in zip(*args) for elem in arg)

numbers = [1, 2, 3]
squares = [1, 4, 9]
qubes = [1, 8, 27]

print(*interleave(numbers, squares, qubes))