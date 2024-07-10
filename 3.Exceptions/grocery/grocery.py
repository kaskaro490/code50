def main():

    grocerylist = {}

    while True:
        try:
            item = item_to_list(input("").upper())

        except EOFError:
            break
        except:
            pass

    grocerylist2 = dict(sorted(grocerylist.items()))
    print(grocerylist2)

# Fonction pour ajouter les item au dictionnaire
def item_to_list(item):
    if not item in grocerylist:
        list[item] = 1
    elif item in dict:
        list[item] += 1








main ()
