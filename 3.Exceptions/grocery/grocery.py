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

    print(grocerylist)

    grocerylist2 = dict(sorted(grocerylist.items()))
    print(grocerylist2)


def item_to_list(grocerylist, item):  # Fonction pour ajouter les item au dictionnaire
    if item not in grocerylist:
        grocerylist[item] = 1
        print(f"{item} added")
    elif item in dict:
        grocerylist[item] += 1
        print(f"{item} increment")



main ()
