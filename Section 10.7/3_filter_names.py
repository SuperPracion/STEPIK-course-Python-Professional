def filter_names(names, ignore_char, max_names):
    filtred_dig = (name for name in names if all([char.isalpha() for char in name]))
    filterd_ignore = (name for name in filtred_dig if name[0].lower() not in ignore_char.lower())

    for _ in range(max_names):
        try:
            yield next(filterd_ignore)
        except:
            continue

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 200))