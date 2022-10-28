from zipfile import ZipFile

def extract_this(zip_name, *args):
        if not args:
            args = None

        with ZipFile(zip_name) as file:
            file.extractall(members=args)

extract_this('workbook.zip', 'earth.jpg', 'exam.txt')