# Zad1
lista = [a for a in range(0, 31) if a % 4 == 0]
print(lista)
plik = open('Zadanie1.txt', 'w')
plik.writelines(str(lista))
plik.close()

# Zad2
plik = open('Zadanie1.txt','r')
zawartosc = plik.read()
print(zawartosc)
plik.close()

# Zad3
with open('Zadanie1.txt', 'r+') as plik:
    plik.write("Zapisany tekst do pliku")

# zapis został dokonany od początku pliku, po zapisaniu komunikatu do pliku
# wskaźnik został przesuniety o zadaną długość naszego komunikatu (przy trybie r+)
# a następnie zostały odczytane dane z pliku, aby odczytać całą zawartość pliku
# najlepiej zamknąć plik i otworzyć go ponownie,
# przy trybie w+ jeśli plik istnieje jest czyszczony podczas otwarcia
# przy trybie a+ jeśli plik istnieje i chcemy z niego odczytać dane, za pomocą metody seek(0)
# z argumentem 0 ustawiamy obecną pozycję w pliku
with open('Zadanie1.txt', 'r+') as plik:
    zawartosc = plik.read()
print(zawartosc)
# Zad4
class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed


def wyswietl_produkt(self): print("produkt to {}, w ilości {}{}, przy cenie {}zł za {}".format(self.nazwa_produktu,
                                                                                               self.ilosc,
                                                                                               self.jednostka_miary,
                                                                                               self.cena_jed,
                                                                                               self.jednostka_miary))


def ile_produktu(self):
    print("{} {}".format(self.ilosc, self.jednostka_miary))


def ile_kosztuje(self):
    return self.ilosc * self.cena_jed


produkt = NaZakupy("Ziemiaki", 3, "kg", 2)
wyswietl_produkt(produkt)
ile_produktu(produkt)
print(str(ile_kosztuje(produkt)) + " zł")
produkt1 = NaZakupy("Gazeta", 2, "szt.", 3)
wyswietl_produkt(produkt1)
# Zad5
class CiagiA:
    def __init__(self, a1, r, n):
        self.a1 = float(a1)
        self.a2 = float(a1 + r)
        self.a3 = float(a1 + 2 * r)
        self.r = float(r)
        self.n = float(n)

    def wyswietl_dane(self):
        print(self.a1)
        print(self.a2)
        print(self.a3)
        print(self.r)
        print(self.n)

    def pobierz_elementy(self):
        self.a1 = float(input("Podaj a1:"))
        self.a2 = float(input("Podaj a2:"))
        self.a3 = float(input("Podaj a3:"))

    def pobierz_parametry(self):
        self.a1 = float(input("Podaj a1:"))
        self.r = float(input("Podaj r:"))
        self.n = float(input("Podaj n:"))

    def policz_sume(self):
        suma = ((2 * self.a1 + (self.n - 1) * self.r) / 2) * self.n
        print(suma)

    def policz_elementy(self):
        print(self.a1 + (self.n - 1) * self.r)


#           (a1,r,n)
ciag = CiagiA(1, 1, 7)
ciag.wyswietl_dane()
ciag.pobierz_elementy()
ciag.pobierz_parametry()
# ciag.wyswietl_dane()
ciag.policz_sume()
ciag.policz_elementy()


# Zad 6
class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y = self.y + (ile_krokow * self.krok)
        self.x = self.x

    def idz_w_dol(self, ile_krokow):
        self.y = self.y - (ile_krokow * self.krok)
        self.x = self.x

    def idz_w_lewo(self, ile_krokow):
        self.y = self.y
        self.x = self.x - (ile_krokow * self.krok)

    def idz_w_prawo(self, ile_krokow):
        self.y = self.y
        self.x = self.x + (ile_krokow * self.krok)

    def pokaz_gdzie_jestes(self):
        print("współrzędne robaczka to x={} y={}".format(self.x, self.y))


robak = Robaczek(1, 0, 1)
robak.pokaz_gdzie_jestes()
robak.idz_w_gore(5)
robak.pokaz_gdzie_jestes()
robak.idz_w_lewo(3)
robak.pokaz_gdzie_jestes()
robak.idz_w_dol(2)
robak.pokaz_gdzie_jestes()
robak.idz_w_prawo(4)
robak.pokaz_gdzie_jestes()