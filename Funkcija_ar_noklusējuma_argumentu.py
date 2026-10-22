def cena_ar_atlaidi(cena, atlaide=10):
    return cena * (1 - atlaide / 100)

pirmais_rezultats = cena_ar_atlaidi(100)
print("Cena ar pirmo atlaidi:", pirmais_rezultats)

otrais_rezultats = cena_ar_atlaidi(100, 25)
print("Cena ar otru atlaidi:",otrais_rezultats)