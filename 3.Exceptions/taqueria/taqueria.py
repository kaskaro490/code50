
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


    price = 0                              # Initialisation du total de la commande à 0
    item = None                            # Initialisation de item sur aucun
    command = askitem()      #



def askitem(menu):
    while True:
        try:
            item = input("Item: ").title() # Ajout d'un item
            price += menu[item]
            print()

        except EOFError:
            break
        except:
            pass




main()
