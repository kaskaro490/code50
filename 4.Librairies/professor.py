import random

def main():
    while True:
        try:
            levelselect = get_level("Level: ") # Demander à l'utilisateur de saisir un niveau (1, 2 ou 3) jusqu'à ce qu'une entrée valide soit reçue.
            if bit levelselect is False: # Vérifier la validité du niveau demandé.
                problems(levelselect)
            else:
                raise ValueError

        except ValueError:
            pass
        except EOFError:
            break



def problems(levelselect):
    attempts = 0
    good_answers = 0
    wrong_answers = 0
    while True:
        try:
            if good_answers + wrong_answers != 10: # Nombre de problèmes inférieur à 10

                x = generate_integer(levelselect) # Générer un x aléatoire entre 0 et 9
                y = generate_integer(levelselect) # Générer un y aléatoire entre 0 et 9

                while attempts < 4: # Nombre de tentatives entre 1 et 3
                    try:
                        answer = int(input(f"{x}+{y}= "))
                        attempts += 1
                        if answer == (x + y):
                            attempts = 0
                            good_answers += 1
                            break
                        elif attempts == 3:
                            wrong_answers += 1
                            print(x+y)
                            break
                    except EOFError:
                        break
                    except:
                        pass
            else:
                print(f"Score: {good_answers}")
                break
        except EOFError:
            break



def generate_integer(l): # Retourner un entier non négatif généré aléatoirement avec le nombre de chiffres spécifié en fonction du niveau.

    if l == 1:
        result = random.randint(0,9)
        return int(result)

def get_level(l): # Valider l'entrée du niveau de l'utilisateur, retournant 1, 2 ou 3.

    userinput = int(input(l))

    if 0 < userinput < 4:
        return userinput
    else:
        return False


if __name__ == "__main__":
    main()




