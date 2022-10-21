import time
from math import factorial


# def factorial_recurrent(n):  # рекурсивная функция
#     if n == 0:
#         return 1
#     return n * factorial_recurrent(n - 1)
#
#
# def factorial_classic(n):  # итеративная функция
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# def math_factorial(n):
#     return factorial(n)
#
#
# def for_and_append():                            # с использованием цикла for и метода append()
#     iterations = 10_000_000
#     result = []
#     for i in range(iterations):
#         result.append(i + 1)
#     return result
#
#
# def list_comprehension():                        # с использованием списочного выражения
#     iterations = 10_000_000
#     return [i + 1 for i in range(iterations)]


def for_and_append(iterable):             # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):         # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):              # с использованием встроенной функции list()
    return list(iterable)

def get_the_fastest_func(funcs, arg):
    mass_times = []

    for func in funcs:
        start = time.perf_counter()
        func(range(100000))
        end = time.perf_counter()

        mass_times.append(end - start)

    return funcs[mass_times.index(min(mass_times))]


print(get_the_fastest_func([for_and_append, list_comprehension, list_function], 0))
