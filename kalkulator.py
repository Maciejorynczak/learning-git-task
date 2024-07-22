import logging
#logger
logging.basicConfig(level=logging.INFO, format='%(message)s')

#działąnia matematyczne
def dodawanie (a, b):
    return a + b

def odejmowanie(a,b):
    return a - b

def mnozenie(a,b):
    return a * b 

def dzielenie(a,b):
    return a / b
# Typy dzialan
dzialanie = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
# Pobieranie dwóch liczb
liczba1 = float(input("Podaj liczbe 1: "))
liczba2 = float(input("Podaj liczbe 2: "))

if dzialanie == 1:
    logging.info(f"Dodaję {liczba1:.2f} i {liczba2:.2f}")
    wynik = dodawanie(liczba1, liczba2)
elif dzialanie == 2:
    logging.info(f"Odejmuję {liczba2:.2f} od {liczba1:.2f}")
    wynik = odejmowanie(liczba1, liczba2)
elif dzialanie == 3:
    logging.info(f"Mnożę {liczba1:.2f} przez {liczba2:.2f}")
    wynik = mnozenie(liczba1, liczba2)
elif dzialanie == 4:
    logging.info(f"Dzielę {liczba1:.2f} przez {liczba2:.2f}")
    wynik = dzielenie(liczba1, liczba2)
else:
    wynik = "Niepoprawny wybór działania!"

print(f"Wynik to: {wynik:.2f}" if isinstance(wynik, float) else wynik)