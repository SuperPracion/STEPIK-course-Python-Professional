files = {}


def to_bytes(weight, type):
    num_of_transfers = {'B': 0, 'KB': 1, 'MB': 2, 'GB': 3}
    for _ in range(num_of_transfers[type]):
        weight *= 1024

    return weight


def to_maxima_file_size_type(weight):
    num_of_transfers = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB'}
    count = 0
    while weight // 1024:
        weight /= 1024
        count += 1

    return [round(weight), num_of_transfers[count]]


with open('files.txt', 'rt', encoding='utf-8') as file:
    content = file.readlines()

    for line in content:
        file, weight, type = line.split()
        extension = file[file.index('.'):]
        files.setdefault(extension, []).append((file, to_bytes(int(weight), type)))

for expansion in sorted(files.items(), key=lambda x: x[0]):
    total = 0
    for file in sorted(expansion[1]):
        print(file[0])  # file name
        total += file[1]  # file weight

    file_info = to_maxima_file_size_type(total)

    print('----------')
    print(f'Summary: {file_info[0]} {file_info[1]}')
    print()
