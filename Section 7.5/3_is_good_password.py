import sys


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError('LengthError')

    if string == string.lower() or string == string.upper():
        raise LetterError('LetterError')

    if string.isalpha():
        raise DigitError('DigitError')

    return True


for string in sys.stdin:
    try:
        is_good_password(string.strip())
        print('Success!')
        break
    except Exception as e:
        print(*e.args)
