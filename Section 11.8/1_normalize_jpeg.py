import re

def normalize_jpeg(filename):
    return re.sub(r'\.\w+$', '.jpg', filename, re.IGNORECASE)

print(normalize_jpeg('stepik.jPeG'))
print(normalize_jpeg('mountains.JPG'))
print(normalize_jpeg('windows11.jpg'))