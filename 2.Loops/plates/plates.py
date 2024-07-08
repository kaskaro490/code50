def main():

    plate = input("Plate: ")
    c

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if

def len_plate_minmax(plate):
    #Vérifier que le nom contienne bien entre 2 et 6 caractères
    if 2<= len(plate) <=6:
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
    for i in range(2, len(plate) - 1):
        if plate[i].isdigit():
            start = i
            while i < len(plate) and plate[i].isdigit():
               i += 1
            end = i
            if plate[start -1].isalpha() and plate[end].isalpha():
                return False
            elif plate[start == 0]:
                return False


main()
