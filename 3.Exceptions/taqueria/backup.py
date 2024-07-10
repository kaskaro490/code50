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

    price = 0  # Initialisation du total de la commande à 0

    while True:
        try:
            price = askitem(menu, price)
        except EOFError:
            # Afficher le total de la commande après la fin de la saisie
            print(f"Total: ${price:.2f}")
            break
        except KeyError:
            # Gérer les cas où l'item n'est pas dans le menu
            print("Item not found. Please enter a valid menu item.")
        except Exception as e:
            # Gérer toute autre exception
            print(f"An error occurred: {e}")

def askitem(menu, price):
    item = input().title()  # Ajout d'un item au panier sans le prompt "Item:"
    if item in menu:
        price += menu[item]
    else:
        raise KeyError(f"Item '{item}' not found in menu.")
    return price

main()
