print("opdracht 1")
x = 18
if x == 18:
	print('de waarde van x = 18')
#Je ook variable zetten

print("opdracht 2")
a = input("Print a: ")
b = input("Print b: ")

if b > a:
  print("b is groter dan a")
elif a == b:
  print("a en b zijn gelijk")
else:
  print("a is groter dan b")

print("opdracht 3")
leeftijd = int(input("Hoe oud ben jij?: "))

if 16 < leeftijd:
    print("Gefeliciteerd, je mag je brommerrijbewijs halen.")
elif 16 > leeftijd:
    print("Helaas, je zult nog even moeten wachten.")

print("opdracht 4")
a = input("Print a: ")
b = input("Print b: ")

if b > a:
  print("b is groter dan a")
elif a > b:
   print("a is groter dan b")
elif b >= a:
   print("of gelijk of b groter dan a")
elif a >= b:
   print("of gelijk of a groter dan b")
elif a == b:
  print("a en b zijn gelijk")
elif a // b:
  print("a is gedeeld en afgerond b")

print("opdracht 5")

a = input("Print a: ")
b = input("Print b: ")
c = input("Print c: ")

if b > a:
    print("b is groter dan a")
elif a == b:
    print("a en b zijn gelijk")
else:
    print("a is groter dan b")

if c > b:
    print("c is groter dan b")
elif c > a:
    print("c is groter dan a")
elif c == a:
    print("c en a zijn gelijk")
else:
    print("c en b zijn gelijk")
