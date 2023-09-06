print("opdracht 1")
cijfer = int(input("Random cijfer: "))

if cijfer == 1:
    print("zeer slecht")
elif cijfer == 2:
    print("slecht")
elif cijfer == 3:
    print("gering")
elif cijfer == 4:
    print("onvoldoende")
elif cijfer == 5:
    print("bijna voldoende")
elif cijfer == 6:
    print("voldoende")
elif cijfer == 7:
    print("ruim voldoende")
elif cijfer == 8:
    print("goed")
elif cijfer == 9:
    print("zeer goed")
elif cijfer == 10:
    print("uitmuntend")
else:
    print("Dat kan niet")

print("opdracht 1")
# Opdracht 2:
# Oh ja: we (oefenen het) formatteren het ook nog even netjes:
# Is je cijfer 6 of groter dan print je:
# "Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}"

# Heb je lager dan een 6 gescoord dan wordt het: 
# "Jammer, {omschrijving} je resultaat is een {cijfer}"

# Zorg ervoor dat een gebruiker een cijfer tussen 1 en 10 kan invoeren. 
# Wordt het getal te groot of te klein dan moet je een melding geven: 'Dit kan ik niet omzetten!'

print("Opdracht 2")
cijfer = int(input("Random cijfer: "))


if cijfer == 1:
    omschrijving = "zeer slecht"
elif cijfer == 2:
    omschrijving = "slecht"
elif cijfer == 3:
    omschrijving = "gering"
elif cijfer == 4:
    omschrijving = "onvoldoende"
elif cijfer == 5:
    omschrijving = "bijna voldoende"
elif cijfer == 6:
    omschrijving = "voldoende"
elif cijfer == 7:
    omschrijving = "ruim voldoende"
elif cijfer == 8:
    omschrijving = "goed"
elif cijfer == 9:
    omschrijving = "zeer goed"
elif cijfer == 10:
    omschrijving = "uitmuntend"
else:
    print('Dit kan ik niet omzetten!')

if cijfer >= 6:
    print(f"Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}")
elif cijfer <= 6:
    print(f"Jammer, {omschrijving} je resultaat is een {cijfer}")