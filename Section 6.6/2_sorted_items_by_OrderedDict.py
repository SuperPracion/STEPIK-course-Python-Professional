from collections import *

data = OrderedDict(key1='value1', key2='value2', key3='value3', key4='value4')
new_data = OrderedDict()

for i in range(len(data)):
    key, value = data.popitem(last=(i % 2 == 1))
    new_data[key] = value

print(new_data)
