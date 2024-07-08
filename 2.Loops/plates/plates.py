# Demander le nom de plaque de l'utilisateur et lui donne rle résultat
def main():
    plate = input("Plate: ").upper()


    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

