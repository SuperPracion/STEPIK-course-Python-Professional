import itertools

def get_biggest(numbers):
    if numbers:
        return int(''.join(map(str, sorted(numbers, key=lambda x: str(x) * len(str(max(numbers))), reverse=True))))
    else:
        return -1

print(get_biggest([0, 0, 0, 0, 0, 0]))
