"""
Zadatak 1.4.2 Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja
nekakvu ocjenu i nalazi se izmedu 0.0 i 1.0. Ispišite kojoj kategoriji pripada ocjena na temelju ¯
sljedecih uvjeta: ´
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe).
Takoder, ako je broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovaraju ¯ cu poruku.
"""

def dodijeli_ocjenu(postotak):
    if postotak >= 0.9:
        return "A"
    elif postotak >= 0.8:
        return "B"
    elif postotak >= 0.7:
        return "C"
    elif postotak >= 0.6:
        return "D"
    else:
        return "F"

try:
    postotak = input()
    if 0.0 <= postotak <= 1.0:
        print(f"Ocjena: {dodijeli_ocjenu(postotak)}")
    else:
        print("Greška: Uneseni broj nije u rasponu 0.0 - 1.0.")
except ValueError:
    print("Greška: Unesite broj.")
