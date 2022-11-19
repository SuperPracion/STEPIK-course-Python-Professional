import string

def verification(login, password, success, fuilure):
    conditions = {string.ascii_letters: 'в пароле нет ни одной буквы',
                  string.ascii_uppercase: 'в пароле нет ни одной заглавной буквы',
                  string.ascii_lowercase: 'в пароле нет ни одной строчной буквы',
                  string.digits: 'в пароле нет ни одной цифры'}

    for condition in conditions:
        if not any(map(lambda x: x in condition, password)):
            return fuilure(login, conditions[condition])

    success(login)