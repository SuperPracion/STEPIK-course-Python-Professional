def spell(*args):
    out_dict = {}
    for word in args:
        if out_dict.get(word[0].lower(), 0) < len(word):
            out_dict[word[0].lower()] = len(word)

    return out_dict

    # sort_args = sorted([x.lower() for x in args], key=len, reverse=True)
    # args = [x.lower() for x in args]
    #
    # for key in args:
    #     out_dict[key[0]] = len(max(sort_args, key=lambda x: x[0] == key[0], *sort_args))
    #
    # return out_dict

words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))