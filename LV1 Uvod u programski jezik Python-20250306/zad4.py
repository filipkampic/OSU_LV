"""
Zadatak 1.4.4 Napišite Python skriptu koja ce u ´ citati tekstualnu datoteku naziva ˇ song.txt.
Potrebno je napraviti rjecnik koji kao klju ˇ ceve koristi sve razli ˇ cite rije ˇ ci koje se pojavljuju u ˇ
datoteci, dok su vrijednosti jednake broju puta koliko se svaka rijec (klju ˇ c) pojavljuje u datoteci. ˇ
Koliko je rijeci koje se pojavljuju samo jednom u datoteci? Ispišite ih.
"""

import string

def brojanje_rijeci(filename):
    broj_rijeci = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                rijeci = line.split()
                rijeci = [rijec.strip('.,!;:').lower() for rijec in rijeci]
                for rijec in rijeci:
                    if rijec in broj_rijeci:
                        broj_rijeci[rijec] += 1
                    else:
                        broj_rijeci[rijec] = 1

        jedinstvene_rijeci = [rijec for rijec, broj in broj_rijeci.items() if broj == 1]
        print(f"Broj riječi koje se pojavljuju samo jedanput: {len(broj_rijeci)}")
        print(f"Te riječi su: {jedinstvene_rijeci}")

    except FileNotFoundError:
        print(f"Greška: Datoteka '{file}' nije pronađena.")
        return {}
    return broj_rijeci

brojanje_rijeci("song.txt")