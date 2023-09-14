# # # Cijfers voor proefwerken en tentamens vallen tussen nul en 10 (inclusief nul en 10), en worden altijd afgerond op halve punten.

# # # De Amerikaanse stijl van beoordelen gebruikt letters.

# # # Ter vergelijking,de cijfers 8.5 tot en met 10 zijn in Amerika 
# “A,” 7.5 en 8 zijn “B," 6.5 en 7 zijn “C,” 5.5 en 6 zijn “D,” en 5 en lager is “F.”
 

# # # Schrijf code die deze vertaling van cijfers naar letters maakt, waarbij de gebruiker gevraagd wordt om het cijfer in te geven. 
# # Als de gebruiker een cijfer buiten het gegeven bereik ingeeft, moet je een foutmelding geven.

cijfer = float(input("Random cijfer: "))

if cijfer in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
  if cijfer >= 8.5 and cijfer <= 10:
        print("A")
elif cijfer >= 7.5 and cijfer <= 8:
    print("B")
elif cijfer >= 6.5 and cijfer <= 7:
    print = ("C")
elif cijfer >= 5.5 and cijfer <= 6:
    print("D") 
elif cijfer <= 5:
    print("F")
else:
    print("Dat kan je niet omzetten")


