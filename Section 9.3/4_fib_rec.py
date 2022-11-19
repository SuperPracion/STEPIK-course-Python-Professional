fib = lambda n, x=0, y=1: fib(n-1, y, y+x) if n > 0 else print(x)

print(fib(1))
print(fib(2))
print(fib(5))