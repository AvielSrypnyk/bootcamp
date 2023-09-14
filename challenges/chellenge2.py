# Maak een programma die de gebruiker om een getal vraagt.

# Aan de hand van het getal dat de gebruiker invoert telt het programma naar 0. 

# Dus bij een invoer van 4 krijgt de gebruiker te zien:

# 4
# 3
# 2
# 1
# 0

# Maar bij het invoeren van -4 krijgt de gebruiker te zien:

# -4
# -3
# -2
# -1
# 0



getal = int(input("Voer een getal in: "))

if getal > 0:
    stap = -1
else:
    stap = 1


while getal != 0:
    print(getal)
    getal += stap
print(0)
