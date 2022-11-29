def palindromes():
    i = 1
    while True:
        if str(i) == str(i)[::-1]:
            yield i
        i += 1

generator = palindromes()

print(next(generator))
print(next(generator))
print(next(generator))