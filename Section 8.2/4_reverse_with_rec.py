def reverse_rec():
    num = input()
    if num != '0':
        reverse_rec()
    print(num)

reverse_rec()

