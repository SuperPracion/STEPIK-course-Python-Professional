def is_good_password(string):
    if all((
            len(string) >= 9,
            any(a.islower() for a in string),
            any(a.isupper() for a in string),
            any(a.isdigit() for a in string))):
        return True
    else:
        return False

print(is_good_password('abc12345678ansdfjkasdkjfbsdk'))