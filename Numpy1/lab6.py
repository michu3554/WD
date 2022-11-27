import numpy as np

# Zad1

a1 = np.arange(3, 48, 3)
print(a1)

# Zad2

a2 = np.arange(1, 2, 0.1)
print(a2)
b = a2.astype('int64')
print(a2.dtype)
print(b.dtype)


# Zad3

def macierz(n):
    for i in range(n):
        x = n * n + 1
        a = np.arange(1, x).reshape(n, n)
    print(a)


macierz(2)
macierz(5)


# Zad4

def generuj(x, y):
    a = np.logspace(1, y, num=y, base=x, dtype=int)
    print(a)


generuj(2, 4)
generuj(2, 10)
generuj(5, 6)
