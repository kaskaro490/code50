# Demander le nom de plaque de l'utilisateur et lui donne rle résultat
def main():
    plate = input("Plate: ").upper()
    charnumber = len(plate)

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#Vérifier qu'un nom de plaque est valide sur tous les paramètres
def is_valid(s, plate):
    #Vérifier que le nom contient bien entre 2 et 6 caractères
    if 2<= charnumber <=6:
        #Vérifier que le début du nom contient bien 2 lettres
        if plate[:2].isalpha():
            #Vérifier que le nom n'a pas de chiffre entre les lettres
            index = 0
            for s in plate:
                if s







main()

