# Zad 1.Napisz skrypt, w którym tworzysz listę z ulubionymi filmami,
# a następnie odwróć całą listę. Po odwróceniu listy dodaj kilka pozycji
# (dodane pozycje mają zostać dodane od 5 indeksu, cała lista mam zawierać
# 10 pozycji)

ulubione_filmy = ["Skazani na Shawshank" "Nietykalni" "Zielona mila" "Ojciec Chrzestny" "Forrest Gump" "Pulp fiction"]
print(ulubione_filmy)
ulubione_filmy.reverse()
print(ulubione_filmy)
ulubione_filmy.insert(5, "Joker")
ulubione_filmy.insert(6, "Pianista")
ulubione_filmy.insert(7, "Incepcja")
ulubione_filmy.insert(8, "Milczenie owiec")
print(ulubione_filmy)

# Zad 2. Stwórz skrypt, w którym utworzysz słownik z filmami z zadania 1. Pomyśl co może być kluczem

slownik_filmow = {'tytul': ulubione_filmy}

slownik_filmow.items()

print(slownik_filmow)

# Zad 3. Stwórz skrypt, gdzie utworzysz słownik z nazwami przedmiotów z obecnego semestru oraz ich skrótami.
# Policz liczbę elementów w słownik

przedmioty = {
    "CAD komputerowe wspomaganie programowania": "CAD",
    "Wizualizacja danych": "WD",
    "Przedmiot humanizujący": "PH",
    "Język angielski": "JA",
    "Rachunek różniczkowy i całkowy": "RRIC",
    "Elementy matematyki dyskretnej": "EMD",
    "Programowanie strukturalne": "PS"
}
print(przedmioty)
print(len(przedmioty))

# Zad 4. Napisz skrypt gdzie wczytasz liczbę dowolnego typu i podnieś ją do tej samej potęgi. Użyj funkcji input.

liczba = input("Podaj dowolną liczbe: ")
liczba = float(liczba)
print(liczba * liczba)

# Zad 5. Napisz skrypt gdzie wczytasz dowolny ciąg znaków,
# i policzysz wystąpienie litery a. Użyj instrukcji readline() i write()).

import sys as system

system.stdout.write("Wpisz dowolny ciąg znaków: ")
ciag_znakow = system.stdin.readline()
print(ciag_znakow.count("a"))

# Zad 6. Wczytaj trzy liczby całkowite a,b,c
# i sprawdź czy liczba a jest parzysta oraz czy jednocześnie b>c

print("Wczytaj trzy liczby całkowite a,b,c: \n")

a = input("a = ")
a = int(a)

b = input("b = ")
b = int(b)

c = input("c = ")
c = int(c)

if a % 2 == 0 and b > c:
    print("prawda")
else:
    print("falsz")

# Zad 7. Napisz skrypt, gdzie stworzysz listę składającą
# się z liczb typu int i float. Następnie za pomocą pętli for
# oblicz sumę elementu obecnego z poprzednim.

lista = [1, 2, 3, 4, 1.1, 1.2, 1.3, 1.4]

i = 0
for i in range(len(lista) - 1):
    suma = lista[i] + lista[i + 1]
    print(suma)

# Zad 8. Napisz skrypt, który
# za pomocą pętli while pobiera 10 liczb,
# a następnie dodaje do listy tylko liczby całkowite

lista1 = []
lista2 = []
i = 0
while i < 10:
    lista2.append(input("Podaj " + str(i + 1) + " liczbe:"))
    i += 1
for i in range(0, len(lista2), 1):
    if int(float(lista2[i])) == float(lista2[i]):
        lista1.append(int(float(lista2[i])))
print(lista1)

# Zad 9. Napisz skrypt, który rysuje następującą literę

# OOOOOO
# O    O
# O    O
# O    O
# O    O
# OOOOOO

lista = [1, 2, 3, 4, 5, 6]

i = 1
for i in range(6):
    if lista[i] % 5 == 1:
        print("000000")
    if lista[i] % 5 != 1:
        print("0    0")

# Zad 10. Napisz skrypt, w którym użytkownik ma podać liczbę i
# który będzie wyłapywał błąd gdy użytkownik poda literę zamiast cyfry.

a = input("Podaj liczbę: ")
try:
    float(a) / float(a)
except ValueError:
    print("blad")
