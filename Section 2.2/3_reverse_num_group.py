n, X, Y, A, B = [int(i) for i in input().split()]
mass = [i for i in range(1, n + 1)]

mass = [*mass[:X - 1], *reversed(mass[X - 1: Y]), *mass[Y:]]
mass = [*mass[:A - 1], *reversed(mass[A - 1: B]), *mass[B:]]

print(*mass)