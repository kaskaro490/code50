import random

x = 0
y = 0
attempts = 0

def main():
    good_answers = 0
    wrong_answers = 0
    try:
            levelselect = get_level("Level: ") # Demander à l'utilisateur de saisir un niveau (1, 2 ou 3) jusqu'à ce qu'une entrée valide soit reçue.
            if not levelselect is False: # Vérifier la validité du niveau demandé.



                    try:
                        if good_answers + wrong_answers != 10: # Nombre de problèmes inférieur à 10
                            x = generate_integer(levelselect) # Générer un x aléatoire entre 0 et 9
                            y = generate_integer(levelselect) # Générer un y aléatoire entre 0 et 9

                            while attempts < 4: # Nombre de tentatives entre 1 et 3
                                try:
                                    answer = int(input(f"{x}+{y}= "))
                                    attempts += 1
                                    if answer == (x + y):
                                        good_answers += 1
                                        attempts = 0
                                        break
                                    elif attempts == 3:
                                        wrong_answers += 1
                                        print(x+y)
                                        break

                                except:
                                    pass
                        else:
                            print(f"Score: {good_answers}")
                            break
                    except ValueError:
                        pass
                    except EOFError:
                        break
            else:
                raise ValueError
    except ValueError:
                pass
    except EOFError:
                break
    except:
                pass

def generate_integer(l): # Retourner un entier non négatif généré aléatoirement avec le nombre de chiffres spécifié en fonction du niveau.

    if l == 1:
        result = random.randint(0,9)
        return int(result)

def get_level(l): # Valider l'entrée du niveau de l'utilisateur, retournant 1, 2 ou 3.

    userinput = int(input(l))

    if 0 < userinput < 4:
        return True
    else:
        return False


if __name__ == "__main__":
    main()






# 2. **Générer des problèmes de mathématiques** :
#    - Générer aléatoirement 10 problèmes mathématiques.
#    - Chaque problème doit être formaté comme `X + Y =`.
#    - `X` et `Y` doivent être des entiers non négatifs avec un nombre de chiffres correspondant au niveau choisi.

# 3. **L'utilisateur résout les problèmes** :
#    - Demander à l'utilisateur de résoudre chaque problème mathématique.
#    - Si la réponse est incorrecte ou n'est pas un nombre, afficher `EEE` et demander à nouveau à l'utilisateur.
#    - Permettre jusqu'à trois essais pour chaque problème.
#    - Après trois tentatives incorrectes, afficher la réponse correcte.

# 4. **Afficher le score de l'utilisateur** :
#    - Garder une trace du nombre de réponses correctes.
#    - À la fin, afficher le score de l'utilisateur sur 10.

