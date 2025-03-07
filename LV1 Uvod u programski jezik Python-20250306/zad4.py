"""
Zadatak 1.4.4 Napišite Python skriptu koja ce u ´ citati tekstualnu datoteku naziva ˇ song.txt.
Potrebno je napraviti rjecnik koji kao klju ˇ ceve koristi sve razli ˇ cite rije ˇ ci koje se pojavljuju u ˇ
datoteci, dok su vrijednosti jednake broju puta koliko se svaka rijec (klju ˇ c) pojavljuje u datoteci. ˇ
Koliko je rijeci koje se pojavljuju samo jednom u datoteci? Ispišite ih.
"""

import string

def brojanje_rijeci(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            rijeci = []
            for line in file:
                line = line.rstrip().split(" ")
                rijeci += line

        jedinstvene_rijeci = list(set(rijeci))
        broj_rijeci = {}
        
        for rijec in jedinstvene_rijeci:
            count = 0
            for r in rijeci:
                if r == rijec:
                    count += 1
            broj_rijeci[rijec] = count

        rijeci_koje_se_pojavljuju_jednom = [rijec for rijec, broj in broj_rijeci.items() if broj == 1]

        print(f"Riječi: {rijeci_koje_se_pojavljuju_jednom}")
        print(f"Broj riječi: {len(rijeci_koje_se_pojavljuju_jednom)}")

    except FileNotFoundError:
        print(f"Greška: Datoteka '{filename}' nije pronađena.")
        return {}
    return broj_rijeci

brojanje_rijeci("song.txt")