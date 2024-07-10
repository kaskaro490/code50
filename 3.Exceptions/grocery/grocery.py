def main():

    grocerylist = {}

    while True:
        try:
            item = input("").upper()
            item_to_list(grocerylist, item)
        except EOFError:
            break
        except:
            pass

    sorted_grocerylist = dict(sorted(grocerylist.items()))


    print("\n".join(f"{value} {key}" for key, value in sorted_grocerylist.items()))


def item_to_list(grocerylist, item):  # Fonction pour ajouter les item au dictionnaire

    if item not in grocerylist:
        grocerylist[item] = 1

    elif item in grocerylist:
        grocerylist[item] += 1




main ()
