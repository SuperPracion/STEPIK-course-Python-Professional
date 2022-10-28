import zipfile

with zipfile.ZipFile('workbook.zip', 'r') as zip_file:
    info = zip_file.infolist()
    need_file = []

    for file in info:
        if file.date_time > (2021, 11, 30, 14, 22, 00) and not file.is_dir():
            need_file.append(file.filename.split('/')[-1])

    print(*sorted(need_file), sep='\n')