import zipfile

with zipfile.ZipFile('workbook.zip', 'r') as zip_file:
    info = zip_file.infolist()
    all_size = 0
    compress_size = 0

    for file in info:
        all_size += file.file_size
        compress_size += file.compress_size

    print(f'Объем исходных файлов: {all_size} байт(а)')
    print(f'Объем сжатых файлов: {compress_size} байт(а)')