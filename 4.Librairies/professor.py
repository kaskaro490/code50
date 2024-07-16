import random
import sys

def main():
    while True:
        try:
            n = get_level("Level: ") # Demander à l'utilisateur de saisir un niveau (1, 2 ou 3) jusqu'à ce qu'une entrée valide soit reçue.
             # Vérifier la validité du niveau demandé.
            problems(n)


        except ValueError:
            pass
        except EOFError:
            break



def problems(n):
    attempts = 0
    good_answers = 0
    wrong_answers = 0
    while True:
        try:
            if good_answers + wrong_answers != 10: # Nombre de problèmes inférieur à 10

                x = generate_integer(n) # Générer un x aléatoire entre 0 et 9
                y = generate_integer(n) # Générer un y aléatoire entre 0 et 9

                while attempts < 4: # Nombre de tentatives entre 1 et 3
                    try:
                        answer = int(input(f"{x}+{y}= "))

                        if answer == (x + y):
                            attempts = 0
                            good_answers += 1
                            break
                        elif attempts == 3:
                            wrong_answers += 1
                            print(x+y)
                            break
                        else:
                            attempts += 1
                    except EOFError:
                        break
                    except:
                        pass
            else:
                print(f"Score: {good_answers}")
                sys.exit()
        except EOFError:
            break



def generate_integer(l): # Retourner un entier non négatif généré aléatoirement avec le nombre de chiffres spécifié en fonction du niveau.

    if l == 1:
        result = random.randint(0,9)
        return int(result)
    elif l == 2:
        result = random.randint(10,99)
        return int(result)
    elif l ==3:
        result = random.randint(100,999)
        return int(result)

def get_level(l): # Valider l'entrée du niveau de l'utilisateur, retournant 1, 2 ou 3.

    n = int(input(l))

    if 0 < n < 4:
        return n
    else:
        raise ValueError


if __name__ == "__main__":
    main()




