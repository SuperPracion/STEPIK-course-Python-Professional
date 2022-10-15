n = int(input())
mass = [i for i in range(1, n + 1)]
len_sequence = {}

for num in sorted(mass, key=lambda x: sum(map(int, list(str(x))))):
    temp = sum(map(int, list(str(num))))
    len_sequence[temp] = len_sequence.get(temp, 0) + 1

print(max(len_sequence.values()))