# Opdracht 1:
# Schrijf een programma dat een lege lijst maakt en vervolgens de gebruiker vraagt om 5 getallen in te voeren. Gebruik de append functie om elk getal aan de lijst toe te voegen en print vervolgens de lijst.
getallen = []

for i in range(5):
    num = int(input("Voer een getal in: "))
    getallen.append(num)

print("De lijst met ingevoerde getallen is:", getallen)

