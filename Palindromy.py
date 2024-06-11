def palindrom(slowo):
    slowo = slowo.replace(" ","").lower()
    return slowo == slowo[::-1]
print(palindrom("kajak"))
print(palindrom("okno"))
print(palindrom("Kobyla ma maly bok"))