from collections import *

# numbers = OrderedDict()
numbers = OrderedDict(two=2, three=3)

numbers['one'] = 1
numbers['zero'] = 0
numbers['ten'] = 10

# del numbers['one']

# numbers.move_to_end('zero', last=True)

print(numbers.popitem())
print(*reversed(numbers))