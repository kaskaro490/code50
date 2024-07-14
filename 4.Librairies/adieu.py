import inflect

p = inflect.engine()

names = []




def main():


    # Une boucle infinie qui demande à user d'écrire des prenoms
    while True:
        try:
            # Chaque prénom est incrémenté à une liste
            newname = input("Name: ").title().strip()
            names.append(newname)

        # Lorsque ctrl+d est tapé, cela affiche "Adieu, adieu, to " suivi de chaque prénoms
        except EOFError:
            # Utilisation de .join() afin d'ajouter 'and' avant le dernier prénom de la liste
            adieu = p.join(names)
            print(adieu)




main()
