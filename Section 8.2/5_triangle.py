def triangle(h):
    if h >= 1:
        print('*' * h)
        triangle(h - 1)

triangle(int(input()))