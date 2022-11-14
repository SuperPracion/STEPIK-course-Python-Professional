def count_nums(number):
    if number:
        return 1 + count_nums(number // 10)
    else:
        return 0

print(count_nums(int(input())))
