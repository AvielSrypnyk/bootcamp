# Opdracht 1:
# je spel (van de vorige les) wordt een hit.
# Gebruikers klagen alleen dat het erg lang duurt voordat ze klaar zijn met raden.
# Na diepgravend onderzoek kom er achter dat je nergens meldt in welke range men kan raden en gebruikers blijken dus te denken dat ze tussen 1 en 100 mogen raden.

# Breid je gereedschap uit met een functie die kan controleren of de ingevoerde waarde in een lijst voorkomt. 
# Je kunt deze functie op twee plaatsen inzetten. Waar? En doe dit dan ook.


import random


min_range = 1
max_range = 100

def is_within_range(guess, min_value, max_value):
    if min_value <= guess <= max_value:
        return True
    else:
        return False

def main():
    GoodStreak = 0
    aantal_keer = 0
    aantal_fouten = 0

    while True:
        while True:
            user_guess = int(input(f"Raad een getal tussen {min_range} en {max_range}: "))
            if is_within_range(user_guess, min_range, max_range):
                break
            else:
                print("Ongeldige invoer. Probeer opnieuw.")

        a = random.randint(min_range, max_range)
        aantal_keer += 1
        
        if user_guess == a:
            print(f"Je hebt het juiste getal geraden! Het is {a}")
            GoodStreak += 1
        else:
            print("Je hebt het getal niet goed geraden. Probeer opnieuw.")
            aantal_fouten += 1
        
        if GoodStreak == 3:
            print(f"Je hebt 3 keer op rij correct geraden! Aantal gespeelde ronden: {aantal_keer}, Aantal fouten: {aantal_fouten}")
            verder = input("Wil je verder spelen (j/n)? ")
            if verder.lower() != "j":
                break

if __name__ == "__main__":
    main()

