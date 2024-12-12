import random

def dob_penzermek():
    eredmeny = []
    i = 0
    while i < 7:  
        dobott_ertek = random.randint(0, 1)  
        if dobott_ertek == 1:
            eredmeny.append("FEJ")
        else:
            eredmeny.append("ÍRÁS")
        i += 1

    eredmeny_str = '-'.join(eredmeny)
    print(eredmeny_str)  
    return eredmeny


penzermek = dob_penzermek()


def fejek_szama(penzermek):
    fej_szam = 0
    for ertek in penzermek:
        if ertek == "FEJ":
            fej_szam += 1
    return fej_szam


def konzol_kiir():
    fej_szam = fejek_szama(penzermek)
    print(f"A fejek száma: {fej_szam}.")


def file_kiir():
    fej_szam = fejek_szama(penzermek)
    with open("fejek.txt", "w") as f:
        f.write(f"A fejek száma: {fej_szam}.\n")




