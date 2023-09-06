print("opdracht 1")
for i in range(1, 26):
    print(i)
 
print("opdracht 2")
amount = 0
while amount <= 20:
    amount += 1
    print("Ik ben hard op weg developer te worden!")

#Het is zelfde 
for i in range(1, 20):
    print("je text")

print("Opdracht 3")
i = 0
count = 0
while i <= 625:
  count+=1
  i += 25
  if i > 625:
    break
  print(f"het past zoveel {count}")

print("Opdracht 4")
i = 0
count = 0
while i <= 625:
  count+=1
  i += 12
  if i > 625:
    break
  print(f"het past zoveel {count}")

print("Opdracht 5")
geld = 10000
rente = 2.8

# Bereken het geld na 5 jaar 
jaar = 0
while jaar < 5:
    geld += (geld / 100 * rente)
    jaar += 1

print(f"Na 5 jaar heb je {round(geld)} euro.")

# Herstel het aanvangsbedrag
geld = 10000
jaar = 0

# Bereken het geld na 15 jaar
while jaar < 15:
    geld += (geld / 100 * rente)
    jaar += 1

print(f"Na 15 jaar heb je {round(geld)} euro.")

