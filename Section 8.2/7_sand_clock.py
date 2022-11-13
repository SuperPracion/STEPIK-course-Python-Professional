def print_clock(h=1):
    levels = [16, 12, 8, 4]

    print(f'{"  " * (h - 1)}{str(h) * levels[h - 1]}')

    if h < 4:
        print_clock(h + 1)
        print(f'{"  " * (h - 1)}{str(h) * levels[h - 1]}')


print_clock()
