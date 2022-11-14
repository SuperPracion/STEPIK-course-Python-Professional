def rec_sum(n):
    if n > 0:
        print(n)
        rec_sum(n - 5)
    print(n)

rec_sum(int(input()))