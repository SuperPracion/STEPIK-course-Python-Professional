import time

def add(a, b, c):
    time.sleep(3)
    return a + b + c

def calculate_it(add, *args):
    start_work = time.monotonic()
    res_add = add(*args)
    end_work = time.monotonic()

    return res_add, end_work - start_work

print(calculate_it(add, 1, 2, 3))