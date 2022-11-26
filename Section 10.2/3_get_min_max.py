def get_min_max(data):
    try:
        return data.index(min(data)), data.index(max(data))
    except:
        return None

data = [2, 3, 8, 1, 7]

print(get_min_max(data))