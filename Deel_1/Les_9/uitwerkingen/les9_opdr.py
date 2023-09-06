# Opdracht 1:
# Leg het verschil uit:
# a=5
# b=3
# c=2
# if (a==6 and b==4 or c==2):
#    print("De conditie is waar")
# else: 
#    print("De conditie is niet waar")	

# En: 
# a=5
# b=3
# c=2
# if (a==6 and (b==4 or c==2)):
#    print("De conditie is waar")
# else:
#    print("De conditie is niet waar")

# (geef met commentaar aan in de code wat het verschil is)

print("opdracht 1")
a=5
b=3
c=2
if (a==6 and b==4 or c==2):
   print("De conditie is waar")
else: 
   print("De conditie is niet waar")	

a=5
b=3
c=2
if (a==6 and (b==4 or c==2)):
   print("De conditie is waar")
else:
   print("De conditie is niet waar")

#De haakjes maaken verschil 

# Opdracht 2:
# De modulo kun je gebruiken om te controleren wat het restant is na een deling met als resultaat een heel getal. 
# Bijv. 	9%2 = 1 
# 	9%5 = 4

# Schrijf een programma wat controleert of een getal (zonder rest) deelbaar is door 7 en 11.
# De ene keer print je: "Dit getal is zonder rest deelbaar door 7 en 11"
# De andere keer: "Dit getal is niet zonder rest deelbaar door 7 en 11"

# Test je programma eens met: 77. (en uiteraard nog met wat andere getallen.) 	  

print("Opdracht 2")
a = 77

if a%7 and a%11:
   print("Dit getal is zonder rest deelbaar door 7 en 11")
else:
   print("Dit getal is niet zonder rest deelbaar door 7 en 11")

# Opdracht 3:
# Schrijf een programma met 3 variabelen:
# leeftijd = 18, snor = j (of n) en diploma = j (of n).

# Je schrijft een programma wat bepaalt of iemand is aangenomen. 
# Je bent aangenomen als je: 18 bent (of ouder) en een snor hebt of onder de 18 met een diploma.

# Let op:
# Je mag maar 1 if statement gebruiken!!!

# Test je programma door de variabelen te wijzigen.

print("Opdracht 3")

leeftijd = int(input("Hoe oud ben je? "))
snor = input("Heb je een snor(j/n)? ")
diploma = input("Heb je een diploma(j/n)?")

if leeftijd >= 18 and snor == "j" and diploma == "j":
   print("Je bent aangenomen")
else:
   print("Jij bent niet aangenomen")
