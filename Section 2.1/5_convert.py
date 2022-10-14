def convert(string):
    return string.upper() if sum(map(lambda x: x.isupper(), string)) > sum(map(lambda x: x.islower(), string)) else string.lower()

print(convert('PI31415!'))