# Demander le nom de plaque de l'utilisateur et lui donne rle résultat
def main():
    plate = input("Plate: ").upper()
    charnumber = len(plate)
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#Vérifier qu'un nom de plaque est valide sur tous les paramètres
def is_valid(s):
    #Vérifier que le nom contien bien entre 2 et 6 caractères
    if 2<= charnumber <=6:



#Vérifier que le nom commence bien par deux lettres

#Vérifier que le nom n'a pas de chiffre entre les lettres

main()

