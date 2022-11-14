def sum_nums(num):
    if not num:
        return 0
    return num % 10 + sum_nums(num // 10)


print(sum_nums(int(input())))
