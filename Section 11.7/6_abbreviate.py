import re


def abbreviate(phrase):
    return ''.join(re.findall(r'\b\w|[A-Z]', phrase)).upper()


print(abbreviate('javaScript object notation'))
print(abbreviate('frequently asked questions'))
print(abbreviate('JS game sec'))
