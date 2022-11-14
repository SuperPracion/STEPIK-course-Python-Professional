def is_power(number):
    if number == 1:
        return True
    else:
        return (number % 2 == 0) and is_power(number // 2)



print(is_power(512))
print(is_power(16))
print(is_power(1))
