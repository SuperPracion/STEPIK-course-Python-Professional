import zipfile

def to_maxima_size(weight):
    num_of_transfers = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB'}
    count = 0
    while weight // 1024:
        weight /= 1024
        count += 1

    return [round(weight), num_of_transfers[count]]

with zipfile.ZipFile('desktop.zip', 'r') as zip_file:
    for file in zip_file.infolist():
        name = [str for str in file.filename.split('/') if str != '']
        size = to_maxima_size(file.file_size)

        print(f'{"  " * (len(name) - 1) if len(name) > 1 else ""}{name[-1]}', end='')

        if size[0] != 0:
            print(f' {size[0]} {size[1]}', end='')

        print()


