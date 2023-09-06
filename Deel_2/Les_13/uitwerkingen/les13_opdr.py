# Opdracht 1:
# Maak een tuple met een lijst kleuren.
# Schrijf code die de gebruiker vraagt om hun naam en favoriete kleur. 
# Controleer of de favoriete kleur van de gebruiker in de tuple voorkomt. 

# Is dat het geval: print klein verhaaltje met daarin de naam naam en kleur.
# Anders print je: "Deze kleur is niet zo geweldig!"


kleuren = ["rood", "blauw", "geel", "groen"]


naam = input("Vul je naam in: ")
kleur = input("Vul je favoriete kleur in: ")


if kleur in kleuren:
    print(f"{naam}, jouw favoriete kleur is {kleur}. Dat is een geweldige kleur!")
else:
    print("Deze kleur is niet zo geweldig!")

