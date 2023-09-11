# Opdracht 1:
# Raad het getal.
# Je gaat een eenvoudig raadspelletje maken. Hiervoor volg je een aantal stappen.
# 1. Maak een variabele aan en vul deze met een random getal tussen 1 en 5.
# 2. Vraag de gebruiker een getal in te voeren tussen 1 en 5.
# 3  a. Goed geraden: print dan in het groen: "Je hebt het getal goed geraden!"
#    b. Niet goed: print dan in het rood: "Je hebt het getal niet goed geraden!"

import random

a = random.randint(1 , 5)
print(a)
vraag = int(input("Voer je nummer van 1 - 5: "))

if vraag == a:
    print("Je hebt het getal goed geraden!")
else:
    print("Je hebt het getal niet goed geraden!")