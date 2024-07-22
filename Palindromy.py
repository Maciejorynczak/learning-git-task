import string
import unicodedata

def palindrom(slowo):
# Normalizowanie tekstu, usuwanie polskich znaków
    slowo = unicodedata.normalize('NFD', slowo)
    slowo = ''.join(c for c in slowo if unicodedata.category(c) != 'Mn')
# Usuwanie wszystkich znaków interpunkcyjnych i spacji
    slowo = slowo.translate(str.maketrans('', '', string.punctuation)).replace(" ","").lower()
    return slowo == slowo[::-1]

print(palindrom("kajak"))
print(palindrom("okno"))
print(palindrom("Kobyla ma maly bok"))
print(palindrom("Zula łowi, tenora bada baronet i woła - luz!"))