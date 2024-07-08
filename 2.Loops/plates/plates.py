def main():

    plate = input("Plate: ")


    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Vérifier si toutes les conditions sont remplies
    return no_middle_numbers(s) # and len_plate_minmax(s) and first_2_letters(s)

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
    for i in range(2, len(s)):
        if s[i].isdigit() and s[i]:
            start = i

            if s[i].isdigit():
                print("i + 1")
                i += 1
            end = i
            print(f"Valeur start: ",{start})
            print(f"Valeur end: ",{end})


            # if s[start - 1].isalpha() and s[end].isalpha():
                 #return False
        else:
            return True
            #elif s[start].isdigit() and s[len(s)].isdigit():
             #   return True


main()
