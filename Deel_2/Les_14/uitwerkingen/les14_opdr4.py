# Opdracht 4:
# Schrijf een programma dat een lege lijst maakt en vervolgens de gebruiker vraagt om 5 woorden in te voeren. 
# Gebruik de append functie om elk woord aan de lijst toe te voegen en gebruik vervolgens een for-lus om door elk woord in de lijst te itereren en print elk woord op een aparte regel.
list = []

for num in range(5):
    list.append(input("Vul een naam: "))

for naam in list:
    print(naam) 