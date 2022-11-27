import math
import random

# Zad1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A = {1-x: x∈<1,10>}
# B = {1,4,16,…,4^7}
# C = {x: x∈B i x jest liczbą podzielną przez 2}

A = [1 - x for x in range(1, 11, 1)]
print(A)

B = [4 ** i for i in range(8)]
print(B)

C = [x for x in B if x % 2 == 0]
print(C)

# Zad2
# Wygeneruj losowo 10 elementów, zapisz je do listy1, następnie wykorzystując Python Comprehension zdefiniuj nową listę,
# która będzie zawierała tylko parzyste elementy

lista1 = []
for i in range(10):
    lista1.append(random.randrange(100))
print(lista1)

parzyste = [i for i in lista1 if i % 2 == 0]
print(parzyste)

# Zad3
# Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu a wartość - jednostka
# w jakiej się je kupuje (np. sztuki, kg itd.). Wykorzystaj Python Comprehension do zdefiniowania nowej listy, gdzie
# będą produkty, których wartość to sztuki.

produkty = {"jajka": "sztuki",
            "chleb": "sztuki",
            "bulki": "sztuki",
            "batonik": "sztuki",
            "pizza": "sztuki",
            "twarog": "kg",
            "maka": "kg",
            "cukier": "kg",
            "pomidory": "kg",
            "ziemniaki": "kg",
            "woda": "litry",
            "mleko": "litry",
            "oranzada": "litry",
            "cola": "litry",
            "kefir": "litry", }
print(produkty)

produkty_sztuki = {key for key, value in produkty.items() if value == "sztuki"}
print(produkty_sztuki)


# Zad4
# Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.

def trojkat_prostokatny(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        print("Trojkat jest prostokatny")
    else:
        print("Trojkat nie jest prostokatny")


trojkat_prostokatny(3, 4, 5)
trojkat_prostokatny(1, 2, 3)


# Zad5
# Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne.

def pole_trapez(a=1, b=2, h=3):
    return ((a + b) * h) / 2


print(pole_trapez())
print(pole_trapez(4, 5, 6))


# Zad6.
# Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy),
# ile (ile elementów ma mnożyć)
# Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10


# Zad7
# Napisz funkcje za pomocą operatora *, która wykona te same działanie co w zadaniu 6.


# Zad8
# Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować listę zakupów w postaci: klucz to nazwa produktu
# a wartość to jego koszt. Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać całościową wartość
# tych produktów.

def zakupy(**produkty):
    wartosc = sum(produkty.values())
    print("Wartosc zakupow wyniosla", wartosc, "zl")


zakupy(chleb=3, mleko=2.5, jajka=10)

# Zad9
# Stwórz pakiet ciągi. Jeden moduł niech dotyczy działań i wzorów związanych z ciągami arytmetycznymi
# a drugi niech dotyczy działań i wzorów związanych z ciągami geometrycznymi

from ciagi import *

print(arytmetyczny.nty_wyraz(1, 16, 10))
print(arytmetyczny.suma(1, 10, 4))
print(arytmetyczny.roznica(2, 5))

print(geometryczny.nty_wyraz(1, 10, 2))
print(geometryczny.suma(1, 10, 1))
print(geometryczny.suma(3, 15, 3))
print(geometryczny.iloraz(3, 9))
