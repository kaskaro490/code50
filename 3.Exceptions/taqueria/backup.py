def totalcommand(menulower, total): # Fonction de prise de commande
    while True:

        try:

            item = input("Item: ").lower() # Ajout d'un item
            if item in menulower:
                total += menulower[item] # ajout du prix de l'article au total de la commande



        except EOFError:
            return print(f"Total: ${total:.2f}")

        except:
            pass
