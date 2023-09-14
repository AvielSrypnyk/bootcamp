# Opdracht 4:
# Verslavend: de gebruikers vinden je game zo leuk dat ze er niet mee kunnen stoppen.
# Pas je game daarom als volgt aan: 
# - goed geraden? Vraag of de gebruiker nog een ronde wil spelen.
# - aan het einde print je het aantal gespeelde ronden en het aantal keer dat de gebruiker fout heeft geraden.
import random



def speel_ronde(a):
    GoodStreak = 0
    aantal_keer = 0
    aantal_fouten = 0

    while GoodStreak < 1:
        vraag = int(input("Voer je nummer van 1 - 5 in: "))
        aantal_keer += 1

        if vraag == a:
            print("Je hebt het juiste getal geraden! Het is", a)
            
            GoodStreak += 1
        else:
            print("Je hebt het getal niet goed geraden. Probeer opnieuw.")
            aantal_fouten += 1

    print(f"Je hebt het correct geraden! Aantal gespeelde ronden: {aantal_keer}, Aantal fouten: {aantal_fouten}")
    return input("Wil je verder spelen (j/n)? ")

while True:
    a = (random.randint(1, 5))
    verder = speel_ronde(a)
    if verder != "j":
        break
