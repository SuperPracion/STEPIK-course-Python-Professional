def is_palindrome(string):
    if string:
        return string[0] == string[-1] and is_palindrome(string[1:-1])
    else:
        return True
