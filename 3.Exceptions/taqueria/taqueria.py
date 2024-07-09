
def main():

    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    menulower = {key.lower(): value for key, value in menu.items()}

    print(menu["Taco"])
    print(menulower["taco"])
    print(f"Total: total(menulower, total)")


def total(menulower, total): # Fonction de prise de commande
    while True:
        try:
            item = input("Item: ").lower() # Ajout d'un Item
            if item in menulower:
                total += menulower["{item}"] # ajout du prix de l'article au total de la commande
                print(f"Total: {total}")
        except EOFError:
            return total

        except:
            if not item in menulower:
               pass



main()
