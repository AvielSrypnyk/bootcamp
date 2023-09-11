def get_integer(vraag):
    try:
        return int(input(vraag))
    except ValueError:
        print("Ongeldige invoer. Voer een geheel getal in.")
        return get_integer(vraag)
print(get_integer("schrijf een numer(integer): "))

def get_float(vraag):
    try:
        return float(input(vraag))
    except ValueError:
        print("Ongeldige invoer. Voer een getal in.")
        return get_float(vraag)
    
print(get_float("schrijf een numer(float): "))