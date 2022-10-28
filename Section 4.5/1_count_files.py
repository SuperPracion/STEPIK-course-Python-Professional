import zipfile

with zipfile.ZipFile('workbook.zip', 'r') as zip_file:
    print(sum([1 for file in zip_file.infolist() if not file.is_dir()]))