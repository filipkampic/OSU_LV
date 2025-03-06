"""
Zadatak 1.4.1 Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je placen ´
po radnom satu. Koristite ugradenu Python metodu ¯ input(). Nakon toga izracunajte koliko ˇ
je korisnik zaradio i ispišite na ekran. Na kraju prepravite rješenje na nacin da ukupni iznos ˇ
izracunavate u zasebnoj funkciji naziva ˇ total_euro.
Primjer:
Radni sati: 35 h
eura/h: 8.5
Ukupno: 297.5 eura
"""

def total_euro(radni_sati, satnica):
    return radni_sati * satnica

radni_sati = float(input("Radni sati: "))
satnica = float(input("eura/h: "))

ukupno = total_euro(radni_sati, satnica)
print(f"Ukupno: {ukupno} eura")
