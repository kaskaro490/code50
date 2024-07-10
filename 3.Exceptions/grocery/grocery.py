def main():

    grocerylist = {}

    while True:
        try:
            item = item_to_list(input("").upper())

        except EOFError:
            break
        except:
            pass
    print(grocerylist)
    grocerylist2 = dict(sorted(grocerylist.items()))
    print(grocerylist2)

# Fonction pour ajouter les item au dictionnaire
def item_to_list(grocerylist, item):
    if item not in grocerylist:
        grocerylist[item] = 1
        prin("{item} added")
    elif item in dict:
        grocerylist[item] += 1
        prin("{item} increment")








main ()
