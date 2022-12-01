def cubes_of_odds(iterator):
    return (num ** 3 for num in iterator if num % 2 == 1)

evens = [2, 4, 6, 8, 10]

print(list(cubes_of_odds(evens)))