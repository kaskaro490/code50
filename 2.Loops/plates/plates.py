# Demander le nom de plaque de l'utilisateur et lui donne rle résultat
def main():
    plate = input("Plate: ").upper()


    if is_valid(s, plate, charnumber):
        print("Valid")
    else:
        print("Invalid")

#Vérifier qu'un nom de plaque est valide sur tous les paramètres
def is_valid(s, plate, charnumber):
    #Vérifier que le nom contient bien entre 2 et 6 caractères
    charnumber = len(plate)
    if 2<= charnumber <=6:
        #Vérifier que le début du nom contient bien 2 lettres
        if plate[:2].isalpha():
            #Vérifier que le nom n'a pas de chiffre entre les lettres
            s = 0
            for s in plate:
                if s.isalpha()
                    s += 1
                elif s.isdigit():
                    s += 1
                    if s.isalpha():
                        return False









main()

