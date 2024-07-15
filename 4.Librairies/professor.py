import random

x = 0
y = 0


def main():
    while True:
        try:
            levelselect = get_level("Level: ") # Demander à l'utilisateur de saisir un niveau (1, 2 ou 3) jusqu'à ce qu'une entrée valide soit reçue.

            while True:
                try:
                    if not levelselect is False: # Vérifier la validité du niveau demandé.
                        x = generate_integer(levelselect)
                        y = generate_integer(levelselect)
                        answer = int(input(f"{x}+{y}= "))
                        good_answers = 0
                        wrong_answers = 0
                        if not good_answers == wrong_answers:
                            if answer == (x + y):
                                good_answers += 1
                            else:
                                wrong_answers += 1

                        else:
                            print(f"")
                except ValueError:
                    print("EEE")
                    pass

        except EOFError:
            break




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

