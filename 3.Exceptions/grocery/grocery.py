def main():

    grocerylist = {}
    item = None

    while True:
        try:
            item_to_list(input("").upper())

        except EOFError:
            break
        except:
            pass
    print(grocerylist)
    grocerylist2 = dict(sorted(grocerylist.items()))
    print(grocerylist2)


def item_to_list(grocerylist, item):
    if item not in grocerylist:
        grocerylist[item] = 1
        prin("{item} added")
    elif item in dict:
        grocerylist[item] += 1
        prin("{item} increment")








main ()
