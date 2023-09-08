# Opdracht 3:
# Schrijf een programma dat een lijst van fruitsoorten maakt en vervolgens de gebruiker vraagt om een fruitsoort in te voeren. 
# Gebruik de remove functie om het opgegeven fruit uit de lijst te verwijderen en print vervolgens de bijgewerkte lijst.
list = []
for woord in range(0 , 5):
    fruitsoorten = input("Vul in fruitsoorten: ")
    verwijderd_woord = list.append(fruitsoorten)
    print(list, woord)

index = int(input("Voer een index in om te verwijderen (0-4): "))

if 0 <= index < len(list):
    list.remove(index)
    print(f"Het verwijderde woord is: {verwijderd_woord}")
    print(f"De bijgewerkte lijst is nu: {list}")
else:
    print("Ongeldige index! Voer een index in tussen 0 en 4.")