import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

# Informacja wyświetlana na początku, dotycząca wyboru działania
dzialanie = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie")

# Prośba o podanie liczb
a = float(input("Podaj składnik 1: "))
b = float(input("Podaj składnik 2: "))

#Obliczenia
if dzialanie == "1":
    logging.info(f"Dodaję {a} i {b}")
    print(f"Wynik to {a + b}")
elif dzialanie == "2":
    logging.info(f"Odejmuję {a} od {b}")
    print(f"Wynik to {a - b}")
elif dzialanie == "3":
    logging.info(f"Mnożę {a} i {b}")
    print(f"Wynik to {a * b}")
elif dzialanie == "4":
        logging.info(f"Dzielę {a} przez {b}")
        print(f"Wynik to {a // b}")
else:
    print("Nie ma takiego działania.")