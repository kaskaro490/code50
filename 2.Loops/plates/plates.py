def main():

    plate = input("Plate: ")
    charnumber = len(plate)
    s = plate.upper()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...

def lenplate():
    #Vérifier que le nom contienne bien entre 2 et 6 caractères

    if 2<= charnumber <=6:
        return True
    else:
        return False

main()
