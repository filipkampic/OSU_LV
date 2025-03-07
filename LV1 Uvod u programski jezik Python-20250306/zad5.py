"""
Zadatak 1.4.5 Napišite Python skriptu koja ce u ´ citati tekstualnu datoteku naziva ˇ SMSSpamCollection.txt
[1]. Ova datoteka sadrži 5574 SMS poruka pri cemu su neke ozna ˇ cene kao ˇ spam, a neke kao ham.
Primjer dijela datoteke:
ham Yup next stop.
ham Ok lar... Joking wif u oni...
spam Did you hear about the new "Divorce Barbie"? It comes with all of Ken’s stuff!
a) Izraˇcunajte koliki je prosjeˇcan broj rijeˇci u SMS porukama koje su tipa ham, a koliko je
prosjeˇcan broj rijeˇci u porukama koje su tipa spam.
b) Koliko SMS poruka koje su tipa spam završava uskliˇcnikom ?
"""

def analyze_sms(filename):
    ham_word_count = 0
    ham_count = 0
    spam_word_count = 0
    spam_count = 0
    spam_exclamation_count = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("\t", 1)
                if len(parts) < 2:
                    continue
                category, message = parts
                word_count = len(message.split())

                if category.lower() == "ham":
                    ham_word_count += word_count
                    ham_count += 1
                elif category.lower() == "spam":
                    spam_word_count += word_count
                    spam_count += 1
                    if message.endswith("!"):
                        spam_exclamation_count += 1
        
        avg_ham_words = ham_word_count / ham_count if ham_count > 0 else 0
        avg_spam_words = spam_word_count / spam_count if spam_count > 0 else 0

        print(f"Proječan broj riječi u ham porukama: {avg_ham_words:.2f}")
        print(f"Proječan broj riječi u spam porukama: {avg_spam_words:.2f}")
        print(f"Broj spam poruka koje završavaju uskličnikom: {spam_exclamation_count}")
    except FileNotFoundError:
        print(f"Greška: Datoteka '{filename}' nije pronađena.")

analyze_sms("SMSSpamCollection.txt")