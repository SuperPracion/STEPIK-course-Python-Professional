def out_nums():
    def rec(step):
        if step <= 100:
            print(step)
            rec(step + 1)
    rec(1)

out_nums()