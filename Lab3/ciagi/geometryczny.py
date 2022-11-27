def nty_wyraz(a1, n, q):
    wyraz = a1 * (q ** (n - 1))
    print(wyraz)


def iloraz(a1, a2):
    ilo = a2 / a1
    print(ilo)


def suma(a1, n, q):
    if q != 1:
        x = a1 * ((1 - q ** n) / (1 - q))
        print(x)
    else:
        x = a1 * n
        print(x)