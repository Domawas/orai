def jatek():
    nev=str(input("Játékos neve: "))
    szerep=str(input("szerepkör: "))
    eletero=0
    if szerep == "varázsló":
        eletero=2
        print(f"Üdvözlünk {nev}, {eletero} életed van!")
    elif szerep == "harcos":
        eletero=10
        print(f"Üdvözlünk {nev}, {eletero} életed van!")
    else:
        eletero=8
        print(f"Üdvözlünk {nev}, {eletero} életed van!")