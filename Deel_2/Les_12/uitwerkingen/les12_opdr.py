# Opdracht 1:
# Schrijf een programma dat de gebruiker vraagt om hun naam en leeftijd in te voeren. Gebruik vervolgens typecasting om de leeftijd van de gebruiker om te zetten in een integer en bereken hoe oud ze zullen zijn over 5 jaar.

naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))

print(f"{naam} je bent over 5 jaar {leeftijd + 5} oud")

# Opdracht 2:
# Schrijf een programma dat de gebruiker vraagt om twee getallen in te voeren. Gebruik vervolgens typecasting om de getallen om te zetten in floats en bereken het gemiddelde van de twee getallen.
getal1 = float(input("Vul een nummer: "))
getal2 = float(input("Vul een nummer: "))

gemiddelde = ((getal1 + getal2) / 2 )
print(f"Het is gemidelde " , gemiddelde)

# Opdracht 3:
# Schrijf een programma dat de gebruiker vraagt om een woord in te voeren. Print vervolgens het volgende:
# "Het woord is: {woord} en bestaat uit {aantal_tekens} tekens."
woord = input("Wat is een woord? ")
aantal_tekens = len(woord)
print(f"Het woord is: {woord} en bestaat uit {aantal_tekens} tekens.")