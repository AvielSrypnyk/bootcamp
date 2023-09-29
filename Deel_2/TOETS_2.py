# Opdracht 1 (schrijf je antwoord als commentaar in een py file):


# a: Waarom is Visual Studio Code handiger voor software development dan bijvoorbeeld Notepad (kladblok)? Noem de voordelen!

# b: Waarom is het goed dat je de commits van jouw code pusht naar github.com?


# Antwoord op vraag 1a:
# Visual Studio Code is handiger voor software development dan Notepad om verschillende redenen:
# 1. Code-autocompletie: VS Code biedt intelligente code-autocompletie, waardoor je sneller kunt coderen.
# 2. Extensies: VS Code extensies erg goede voor verschillende programmeertalen en tools.

# Antwoord op vraag 1b:
# Het is goed om je commits naar GitHub te pushen omdat:
# 1. Back-up: GitHub fungeert als een externe back-up van je code, dus zelfs als je lokale kopie verloren gaat, is je code veilig.
# 2. Versiebeheer: Je kunt de geschiedenis van wijzigingen in je code bijhouden en teruggaan naar eerdere versies indien nodig.

# Opdracht 2
# Maak het commentaar af.
a = 5  # dit is een voorbeeld van het datatype: integer 
b = 10.5  # dit is een voorbeeld van het datatype: float 
c = "Hallo wereld"  # dit is een voorbeeld van het datatype: string 

# Opdracht 3:
# Schrijf code die de waarden van a en b omwisselt. Gebruik daarvoor een extra variabele.
a = 5
b = 10
a, b = b, a
# voeg jouw code toe…
# Controleer met onderstaande code of de waarden correct zijn verwisseld
print(f"a = {a}, b = {b}") # Moet "a = 10 b = 5" printen

# Opdracht 4:

# Los de problemen op (zonder exception handling).
leeftijd = int(input("Hoe oud ben je? "))
jaren_tot_pensioen = 67 - leeftijd  # Bereken jaren tot pensioen
print(f"Dan duurt het nog ongeveer {jaren_tot_pensioen} jaar voordat je met pensioen mag!")
# Is 18 ingevuld? Dan zie je op de terminal: Dan duurt het nog ongeveer 49 jaar voordat je met pensioen mag!

# Opdracht 5: 
# Schrijf een functie die 3 getallen bij elkaar optelt en zorg ervoor
# dat de uitkomst ervan wordt getoond in de print
getal1 = 200
getal2 = 5
getal3 = 12
def som(a, b, c):
    return a + b + c
antwoord = som(getal1, getal2, getal3)
print(f"De som van {getal1} + {getal2} + {getal3} = {antwoord}")


# Opdracht 6:
# Maak de volgende code af:# Je moet bijbetalen als je over je minuten of je GB's heen gaat en geen onbeperkt abonnement hebt.
AANTAL_GB = 20 # Aantal GB data in je bundel
AANTAL_MINUTEN = 200 # Aantal belminuten in je bundel
ONBEPERKT = False # test ook met True
aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))
if not ONBEPERKT and (aantal_minuten_gebeld > AANTAL_MINUTEN or aantal_GB_internet > AANTAL_GB):
    print("Let op: je moet bijbetalen!")
else:
    print("Niet aan de hand gebruik je mobiel lekker verder!")

# Opdracht 7:
# Print onder elkaar de getallen 1-250 met max 2 regels code.

# Lijstcomprehensie om de getallen 1 tot 250 te genereren
for num in range(1, 251):
    print(num)

# Opdracht 8:
# Gegeven is:

lijst_eten = ['appel', 'pannenkoek', 'kiwi', 'hamburger']

# a: print een eenvoudig menu met de volgende layout:

# Onze menukaart:
# appel
# pannenkoek
# kiwi
# hamburger 

# b: Schrijf code die ervoor zorgt dat alleen het eten met de langste naam wordt geprint in de terminal. 
# # Let op: je moet in de code eerst bepalen welk eten de langste naam heeft (en dus niet hardcoded 1 voor de index gebruiken). 
# # test je code door extra eten toe te voegen met een nog langere naam.

# Opdracht a: 
print("Onze menukaart:")
for item in lijst_eten:
    print(item)
    
# Opdracht b zonder 
max_lengte = 0
for item in lijst_eten:
    lengte = len(item)
    if lengte > max_lengte:
        max_lengte = lengte

print("Het eten met de langste naam is:")
for item in lijst_eten:
    if len(item) == max_lengte:
        print(item)


# Opdracht 9:
# Schrijf een programma wat de gebruiker vraagt een cijfer in te voeren via de terminal.
# Dit blijf je herhalen totdat de gebruiker een getal tussen 0 en 10 heeft ingevoerd.
# Voert de gebruiker iets anders in dan een getal: geef een foutmelding.

while True:
    try:
        invoer = int(input("Voer een getal tussen 0 en 10 in: "))
        if 0 <= invoer <= 10:
            break
        else:
            print("Fout: Voer een getal tussen 0 en 10 in.")
    except ValueError:
        print("Fout: Dit is geen geldig getal. Probeer opnieuw.")

print(f"Je hebt het juiste getal ingevoerd: {invoer}")


# Opdracht 10:
# repareer de volgende code:
MAX = 20
getal = int(input("Voer een getal in: ")) 

if getal > MAX:
    print(f"Het getal is groter dan {MAX}")
elif getal < MAX:
    print(f"Het getal is kleiner dan {MAX}")
else:
    print(f"Het getal is gelijk aan {MAX}")
