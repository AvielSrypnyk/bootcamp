# Opdracht 3:
# Je gaat een hulpmiddel schrijven die je bij het programmeren kunt gebruiken. 
# Maak de file: user_input.py.

def get_integer (vraag):
    integer = int(input(vraag))
    return integer

print(get_integer("schrijf een numer(integer): "))

def get_float(vraag):
    returning = float(input(vraag))
    return returning
    
print(get_float("Schrijf een numeriek getal (float): "))

def get_string(vraag):
    returning = str(input(vraag))
    return returning
    
print(get_string("Schrijf een numeriek getal (string): "))

alfabet = "abcdefghijklmnopqrstuvwxyz"

def get_letter(vraag):
    returning = input(vraag).lower()
    if returning in alfabet:
        return returning.capitalize()
    else:
        print("Dit zit niet in het alfabet.")

print(get_letter("Schrijf een (letter): "))

