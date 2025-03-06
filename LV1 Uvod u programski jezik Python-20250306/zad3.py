"""
Zadatak 1.4.3 Napišite program koji od korisnika zahtijeva unos brojeva u beskonacnoj petlji ˇ
sve dok korisnik ne upiše „Done“ (bez navodnika). Pri tome brojeve spremajte u listu. Nakon toga
potrebno je ispisati koliko brojeva je korisnik unio, njihovu srednju, minimalnu i maksimalnu
vrijednost. Sortirajte listu i ispišite je na ekran. Dodatno: osigurajte program od pogrešnog unosa
(npr. slovo umjesto brojke) na nacin da program zanemari taj unos i ispiše odgovaraju ˇ cu poruku
"""

brojevi = []

while True:
    unos = input("Unesite broj: (ili Done za kraj): ")
    if unos.lower() == "done":
        break
    try:
        broj = float(unos)
        brojevi.append(broj)
    except ValueError:
        print("Greška: Upišite broj ili 'Done' za kraj.")

if brojevi:
    ukupno_brojeva = len(brojevi)
    sr_vrijednost = sum(brojevi) / ukupno_brojeva
    min_vrijednost = min(brojevi)
    max_vrijednost = max(brojevi)
    sortirani_brojevi = brojevi.sort()

    print(f"Ukupno brojeva: {ukupno_brojeva}")
    print(f"Srednja vrijednost: {sr_vrijednost}")
    print(f"Minimalna vrijednost: {min_vrijednost}")
    print(f"Maksimalna vrijednost: {max_vrijednost}")
    print(f"Sortirani brojevi: {sortirani_brojevi}")
else:
    print("Niste unijeli nijedan broj.")
    