# Vraag 10 getallen via de input.

# Nadat je 10 getallen hebt opgevraagd, doe je het volgende: 

# print: 
# het grootste getal is: ---
# het kleinste getal is: ---
# het aantal getallen deelbaar door 3 (zonder rest) is: ---
# hint:
# 9 % 3

getal = int(input("Voer het eerste getal in: "))


grootste = getal
kleinste = getal
aantal_deelbaar_door_3 = 0


for i in range(9):
    getal = int(input("Voer een getal in: "))
    

    grootste = max(grootste, getal)
    kleinste = min(kleinste, getal)
    

    if getal % 3 == 0:
        aantal_deelbaar_door_3 += 1

print("Het grootste getal is:", grootste)
print("Het kleinste getal is:", kleinste)
print("Het aantal getallen deelbaar door 3 (zonder rest) is:", aantal_deelbaar_door_3)

