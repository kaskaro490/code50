import random


def main():
    ...


def get_level(): # Valider l'entrée du niveau de l'utilisateur, retournant 1, 2 ou 3.
    ...


def generate_integer(level): # Retourner un entier non négatif généré aléatoirement avec le nombre de chiffres spécifié en fonction du niveau.
    ...


if __name__ == "__main__":
    main()




# 1. **Demander le niveau à l'utilisateur** :
#    - Le programme doit demander à l'utilisateur de saisir un niveau (1, 2 ou 3).
#    - Si l'entrée n'est pas 1, 2 ou 3, demander à nouveau jusqu'à ce qu'une entrée valide soit reçue.

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

# 5. **Structure des fonctions** :
#    - Implémenter `get_level` pour demander et valider l'entrée du niveau de l'utilisateur, retournant 1, 2 ou 3.
#    - Implémenter `generate_integer` pour retourner un entier non négatif généré aléatoirement avec le nombre de chiffres spécifié en fonction du niveau.

# Cette structure garantit que le programme est interactif et éducatif, similaire au jouet original "Little Professor".
