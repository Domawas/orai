class Epulet:
    def __init__(self, nev, varos, orszag, magassag, emeletek, ev):
        self.nev = nev
        self.varos = varos
        self.orszag = orszag
        self.magassag = magassag  
        self.emeletek = emeletek
        self.ev = ev

    def magassag_labban(self):
        return self.magassag * 3.280839895

def beolvas_epuletek(fajlnev):
    epuletek = []
    try:
        with open(fajlnev, 'r', encoding='utf-8') as file:
            next(file) 
            for sor in file:
                adatok = sor.strip().split('$')
                if len(adatok) == 6: 
                    nev, varos, orszag, magassag, emeletek, ev = adatok
                    
                    
                    magassag = float(magassag.replace(',', '.'))  
                    emeletek = int(emeletek)  
                    ev = int(ev)  
                    epuletek.append(Epulet(nev, varos, orszag, magassag, emeletek, ev))
                else:
                    print(f"Hiba: Rossz formátumú sor: {sor}")
    except FileNotFoundError:
        print(f"Hiba: A fájl '{fajlnev}' nem található.")
    except Exception as e:
        print(f"Hiba történt: {e}")
    
    return epuletek


def __str__(self):
        return f"Épület neve: {self.nev}, Város: {self.varos}, Ország: {self.orszag}, Magasság: {self.magassag} m, Emeletek: {self.emeletek}, Év: {self.ev}"



def main():
    
    epuletek_lista = beolvas_epuletek('epulet.txt')

    if epuletek_lista: 
        
        print(f"Az épületek száma: {len(epuletek_lista)}")

        
        magas_epuletek = [e for e in epuletek_lista if e.magassag_labban() > 555]
        print(f"Az 555 lábnál magasabb épületek száma: {len(magas_epuletek)}")

        
        legoregebb_epulet = min(epuletek_lista, key=lambda e: e.ev)
        print(f"A legöregebb épület országa: {legoregebb_epulet.orszag}")
    else:
        print("Nincs adat, amit feldolgozhatnánk.")


if __name__ == "__main__":
    main()

