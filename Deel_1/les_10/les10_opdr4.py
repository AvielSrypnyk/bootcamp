# Opdracht 4.

# Joris de Tester heeft een programma geschreven om de kosten van vloerbedekking te berekenen. Er zijn staffelprijzen (afwijkende prijzen voor grote bestellingen) voor verschillende hoeveelheden. 
# Er zit echter een fout in de code die moet worden verbeterd. Kun jij helpen? 😊

oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig?'))
prijs_m2 = 40

if oppervlakte >= 150:
    prijs_m2 = 35
elif oppervlakte >= 80:
    prijs_m2 = 38

totaal = prijs_m2 * oppervlakte

print(f'Het totaalbedrag voor een oppervlakte van {oppervlakte} m2 is: Eur {totaal}')


