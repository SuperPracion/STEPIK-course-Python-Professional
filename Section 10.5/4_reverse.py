def reverse(sequence):
    for some in sequence[::-1]:
        yield some

generator = reverse('beegeek')

print(type(generator))
print(*generator)