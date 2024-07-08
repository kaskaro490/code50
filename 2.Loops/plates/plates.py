def main():

    plate = input("Plate: ")


    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Vérifier si toutes les conditions sont remplies
    return len_plate_minmax(s) and first_2_letters(s) and no_middle_numbers(s)

def len_plate_minmax(s):
    #Vérifier que le nom contienne bien entre 2 et 6 caractères
    if 2<= len(s) <=6:
        return True
    else:
        return False

def first_2_letters(s):
    #Vérifier que le début du nom contient bien 2 lettres
    if s[:2].isalpha():
        return True
    else:
        return False

def no_middle_numbers(s):
    for i in s:
        if s[i].isdigit():
            start = i
            

main()
