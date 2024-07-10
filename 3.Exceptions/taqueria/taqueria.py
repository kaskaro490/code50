
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
    total = 0
    Total = totalcommand(menulower, total)


def totalcommand(menulower, total): # Fonction de prise de commande
    while True:

        try:

            item = input("Item: ").lower() # Ajout d'un item
            if item in menulower:
                total += menulower[item] # ajout du prix de l'article au total de la commande
                


        except EOFError:
            print(f"\nTotal: ${total}")
            return total

        except:
            pass






main()
