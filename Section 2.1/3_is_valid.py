def is_valid(string):
    # return (4 <= len(string) <= 6) and \
    #        all([x in '1234567890' for x in string]) and \
    #        (' ' not in string)

    return string.isdigit() and len(string) in (4, 5, 6)

print(is_valid('49 83'))