print("opdracht 1")
print( 15+4 ) #Het is plus functie 
print( 15-4 ) #Het is minus functie 
print( 15*4 ) #Het is keer functie  
print( 15/4 ) #Het is delen door
print( 15//4 ) #Delen door met afronden heel getaal
print( 15**4 ) #tot de macht
print( 15%4 ) #Het is een getal dat over blijft

print("opdracht 2")
#spatie mag niet uit met wiskunde
print( 5*2 -3+4/2 )
print( 5*2 - 3+4 / 2 )

#Door de haakjes
print( (5*2) - (3+4) /2 )
print( ((5*2) -(3+4)) / 2 )

print("opdracht 3")
Naam = "Aviel"
print("Hallo " + Naam + ", Ik leer nu programeren.")
#Ja dat werekt best goed

print("opdracht4")
Naam = 252
print("Hallo " + str(Naam) + ", Ik leer nu programeren.")
#Ja dat werekt best goed

print("opdracht5")
a = 25 
b = 5
print(a/b)
#Nee het doet niet want je kan niet delen door null

print("opdracht 6")
#Ik heb paar haakjes verwijderd
print(2*3 /4 + (5 -6/7) *8 )
print( (12*13 /14 + (15 -16) /17) *18 )

print("opdracht 7")
print( (431 / 100) * 100 )#Het is 430,99999...
#Het werkt niet goed bij mij

print("opdracht 8")
print(625//13, 625%13)

print("opdracht 9")

studiejaar = 1357

jouwklass = int(input("hoeveel leerling bij jouw in de klass: "))
sum = studiejaar * jouwklass
print ("het is zoveel:", sum)

print((3.40 + 2.45 + 1.95) / 109 * 9)

print("opdracht 10")
#Ik heb niet goed begrepen
slaaptijd = input("Hoeveel slaap je?: ")
time = input("Hoeveel uren heb je activiteit?: ")
odds = (24 - int(slaaptijd) - int(time))
print("Het is je zit tijd " + str(odds))
week = (int(odds) * 7)
print("Je zit zoveel in een week " + str(week))

jaar = (int(odds) * 365)
print("Je zit zoveel in een jaar " + str(jaar))

#Hier is een goede antwoord
dag = 60 * 60 * 24
week = dag * 7
jaar = week * 52

print(dag, week, jaar)