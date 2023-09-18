# Opdracht 1:
# je spel (van de vorige les) wordt een hit.
# Gebruikers klagen alleen dat het erg lang duurt voordat ze klaar zijn met raden.
# Na diepgravend onderzoek kom er achter dat je nergens meldt in welke range men kan raden en gebruikers blijken dus te denken dat ze tussen 1 en 100 mogen raden.

# Breid je gereedschap uit met een functie die kan controleren of de ingevoerde waarde in een lijst voorkomt. 
# Je kunt deze functie op twee plaatsen inzetten. Waar? En doe dit dan ook.


import random
from termcolor import colored

getal1 = random.randint(1,5)
getal_invullen = True
kansen = 3
Jalist = ["ja", "j", "y", "yes"]
rondes = 1
fouten = 0

print(getal1)
while getal_invullen:
    try:
        raadgetal = int(input("raad een getal tussen 1 en 5 "))
    except ValueError:
        print("vul een getal in tussen 1 en 5! ")

    if raadgetal == getal1:
        print(colored(f"goed geraden", "green"))
        vraag = input("wil je nog potje spelen j/n ").lower()
        rondes += 1
        if vraag in Jalist:
            getal1 = random.randint(1, 5)
            print("Sucsess")
            kansen = 3
        else:
            print("Tot ziens")
            getal_invullen = False

    elif kansen >= 1:
        kansen -= 1
        fouten += 1
        print(colored("verkeerd geraden!", "red"))
        getal_invullen = True

    if kansen == 0:
        vraag = input("wil je nog potje spelen j/n ")
        if vraag in Jalist:
            getal1 = random.randint(1, 5)
            print("Sucsess")
            kansen = 3
        else:
            print("Tot ziens")
            getal_invullen = False

print(f"je hebt {rondes} rondes gespeeld en {fouten} fouten gemaakt ")

