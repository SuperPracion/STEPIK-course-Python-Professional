def traffic(loop):
    def rec(step):
        if step < loop:
            print('Не парковаться')
            rec(step + 1)
    rec(0)

traffic(4)
