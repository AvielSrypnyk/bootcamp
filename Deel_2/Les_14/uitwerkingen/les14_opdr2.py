# Opdracht 2:
# Schrijf een programma dat een lijst van 5 getallen maakt en vervolgens de gebruiker vraagt om een index in te voeren.
#  Gebruik de pop functie om het getal op de opgegeven index uit de lijst te verwijderen en print vervolgens het verwijderde getal en de bijgewerkte lijst.

# Maak een lijst van 5 getallen
getallen = []

for _ in range(5):
    num = int(input("Vul een nummer in: "))
    getallen.append(num)

# Vraag de gebruiker om een index in te voeren
index = int(input("Voer een index in om te verwijderen (0-4): "))

# Controleer of de ingevoerde index geldig is
if 0 <= index < len(getallen):
    verwijderd_getal = getallen.pop(index)
    print(f"Het verwijderde getal is: {verwijderd_getal}")
    print(f"De bijgewerkte lijst is nu: {getallen}")
else:
    print("Ongeldige index! Voer een index in tussen 0 en 4.")
