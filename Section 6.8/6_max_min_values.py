from collections import *

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.min_values = lambda: [(key, value) for key, value in data.items() if value == min(data.values())]
data.max_values = lambda: [(key, value) for key, value in data.items() if value == max(data.values())]