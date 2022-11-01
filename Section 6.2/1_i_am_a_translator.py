from  string import ascii_letters

table = str.maketrans(ascii_letters, input() * 2)

print(input().translate(table))
