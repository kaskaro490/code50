import random


def main():
    while True:
        try:
            level = get_level("Level: ") # Demander à l'utilisateur de saisir un niveau (1, 2 ou 3) jusqu'à ce qu'une entrée valide soit reçue.

            if not get_level() is False: # Vérifier la validité du niveau demandé.



        except:
            pass


    # except ValueError:
           # pass


 def get_level(l): # Valider l'entrée du niveau de l'utilisateur, retournant 1, 2 ou 3.

    userinput = int(input(l))

    if 0 < userinput < 4:
        return userinput
    else:
        return False




def generate_integer(level): # Retourner un entier non négatif généré aléatoirement avec le nombre de chiffres spécifié en fonction du niveau.

    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)

    elif
    elif
    else



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

