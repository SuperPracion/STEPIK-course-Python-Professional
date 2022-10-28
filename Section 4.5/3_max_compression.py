import zipfile


def comp_sort_by_effictiveness(params):
    return params.compress_size / params.file_size


with zipfile.ZipFile('workbook.zip', 'r') as zip_file:
    info = zip_file.infolist()
    all_files = [file for file in info if not file.is_dir()]

    need_file = sorted(all_files, key=lambda x: comp_sort_by_effictiveness(x))[0].filename
    print(need_file.split('/')[-1])

