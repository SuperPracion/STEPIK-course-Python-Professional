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
        raise LengthError

    if string == string.lower() or string == string.upper():
        raise LetterError

    if string.isalpha():
        raise DigitError

    return True
