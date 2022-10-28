import zipfile
import datetime

with zipfile.ZipFile('workbook.zip', 'r') as zip_file:
    info = [file for file in zip_file.infolist() if not file.is_dir()]

    for file in sorted(info, key=lambda x: x.filename.split('/')[-1]):
        print(file.filename.split('/')[-1])
        print(f'  Дата модификации файла: {datetime.datetime(*file.date_time)}')
        print(f'  Объем исходного файла: {file.file_size} байт(а)')
        print(f'  Объем сжатого файла: {file.compress_size} байт(а)', end='\n\n')