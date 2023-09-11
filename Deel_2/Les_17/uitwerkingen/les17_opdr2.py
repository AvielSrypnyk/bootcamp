# Opdracht 2:
# Breid je programma nu zodanig uit dat de gebruiker net zolang moet raden tot hij het juiste getal heeft gevonden.

import random

a = random.randint(1, 5)

while True:
    vraag = int(input("Voer je nummer van 1 - 5 in: "))
    if vraag == a:
        print("Je hebt het juiste getal geraden! Het is", a)
        break
    else:
        print("Je hebt het getal niet goed geraden. Probeer opnieuw.")

    