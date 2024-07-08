def main():

    plate = input("Plate: ")
    charnumber = len(plate)

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...

def lenplate(charnumber):
    #Vérifier que le nom contienne bien entre 2 et 6 caractères

    if 2<= charnumber <=6:
        return True
    else:
        return False

def first_2_letters(plate):
    #Vérifier que le début du nom contient bien 2 lettres
    if plate[:2].isalpha():
        return True
    else:
        return False

def no_middle_numbers(plate):
    length = len(plate)
    for i in range(1 < length - 1):
        if plate[i].isdigit():
            

main()
