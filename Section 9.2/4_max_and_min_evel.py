def get_solution(expression, x):
    return eval(expression)


expression = input()
start, end = [int(i) for i in input().split()]

print(f'Минимальное значение функции {expression} на отрезке [{start}, {end}] равно {min([get_solution(expression, i)for i in range(start, end + 1)])}')
print(f'Максимальное значение функции {expression} на отрезке [{start}, {end}] равно {max([get_solution(expression, i)for i in range(start, end + 1)])}')
