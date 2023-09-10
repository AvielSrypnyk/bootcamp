# Opdracht 1:
# Schrijf een functie met twee parameters (integers).
# De functie retourneert de som van de twee parameters.

def som_van_twee_getallen(getal1 , getal2):
    som = getal1 + getal2
    return som

getal1 = 5
getal2 = 3
resultaat = som_van_twee_getallen(getal1, getal2)
print(f"De som van {getal1} en {getal2} is {resultaat}")