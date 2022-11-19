def new_print(*args, sep=' ', end='\n'):
    args = map(lambda x: x.upper() if hasattr(x, 'upper') else x, args)
    old_print(*args, sep=sep.upper(), end=end.upper())

old_print = print
print = new_print

