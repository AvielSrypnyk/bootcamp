# Opdracht 3:
# Zorg ervoor dat je drie rondjes achter elkaar kunt spelen en er dus drie keer een getal moet worden geraden.

import random

a = random.randint(1, 5)
GoodStreak = 0 

while GoodStreak < 3:
    vraag = int(input("Voer je nummer van 1 - 5 in: "))
    if vraag == a:
        print("Je hebt het juiste getal geraden! Het is", a)
        GoodStreak += 1
    else:
        print("Je hebt het getal niet goed geraden. Probeer opnieuw.")
        GoodStreak = 0