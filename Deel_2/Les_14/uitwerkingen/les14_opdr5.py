# Opdracht 5:
# Schrijf een programma dat een lijst van 5 namen maakt en vervolgens de gebruiker vraagt om een naam in te voeren. 
# Gebruik de remove functie om de opgegeven naam uit de lijst te verwijderen als deze voorkomt en print vervolgens de bijgewerkte lijst.
#  Als de opgegeven naam niet in de lijst voorkomt, 
# gebruik dan de append functie om deze aan de lijst toe te voegen en print vervolgens de bijgewerkte lijst.
namen = []

for _ in range(5):  
    naam = input("Vul namen: ")
    namen.append(naam)  


remove_index = int(input("Enter an index to remove (0-4): "))


if 0 <= remove_index < len(namen):
    removed_naam = namen.pop(remove_index)  
    print(f"{removed_naam} has been removed from the list.")
    print(f"The updated list is now: {namen}")
else:
    print("Ongeldige index! Voer een index in tussen 0 en 4.")


