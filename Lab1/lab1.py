# zad 1

a = 1
b = 2
c = 1.1
d = 1.2
e = 1+1j
f = 1+2j
g = "napis"
h = "napis2"

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

# zad 2

a = 10
b = 2

dodawanie = a + b
odejmowanie = a - b
mnozenie = a * b
dzielenie = a / b
dzielenie_calkowite = a // b
reszta = b % a
potega = a ** b
print(dodawanie)
print(odejmowanie)
print(mnozenie)
print(dzielenie)
print(dzielenie_calkowite)
print(reszta)
print(potega)

# zad3

a = 5

a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)
a **= 2
print(a)
a %= 2
print(a)

# zad4

from math import *

print(e ** 10)

print(log(5+sin(radians(8)**2)**(1/6)))

print(floor(3.55))
print(ceil(4.80))

# zad5

imie, nazwisko = "MICHAŁ", "SIEKLICKI"
print(imie.capitalize() + " " + nazwisko.capitalize())

# zad 6

tekst = "M.A.T  White o o o o la la la la"

print(tekst.count("o"))
print(tekst.count("la"))

# zad7

lancuch = "Ala ma kota"
print(lancuch[1])
print(lancuch[-2])

# zad8

tekst = "M.A.T  White o o o o la la la la"
print(tekst.split())

# zad 9

a = "formatowanie"
b = 3.14
c = 0x123AF
print('To jest podstawowe %(a)s lancucha.' % {'a': a})
print('Przyblizenie liczby pi wynosi: %(b)f. ' % {'b': b})
print('Liczba 74671 w systemie szczestnastkowym wynosi: %(c)X. ' % {'c': c})