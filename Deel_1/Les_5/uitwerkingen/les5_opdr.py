print("opdracht 1")
naam = 252
print("Hallo " + str(naam) + ", ik leer nu programeren ")

print("opdracht 2")
print( 3* "hallo" )
#Het doet drie keer hallo

print("opdracht 3")
#Gewoon variable met input
var1 = int(input("schrijf een nummer "))
var2 = int(input("schrijf een nummer "))
var3 = int(input("schrijf een nummer "))

#Voor gemiddelde cijfer moet je sum bereikenen
sum = (var1 + var2 + var3)
gemiddelde = (sum / int(3) ) #En daarna gewoon delen door 
print(round(gemiddelde))

print("opdracht 4")
straal = 20
pi = 3.14159
print("Het is oppervlakte " + str(straal * straal * pi))

straal = int(input("Schrijf een straal: "))
pi = 3.14159
print("Het is oppervlakte " + str(straal * straal * pi))