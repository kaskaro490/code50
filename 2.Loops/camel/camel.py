def main():

    # Demander le nom en camelCase
    name = input("What is the name of the variable? ")
    snakename = underscore(name)
    print(snakename)

# Trouver la position de la lettre majuscule dans le nom
def underscore(name):
    result = []
    for letter in name:
        if letter.isupper():
            result.append("_")
            result.append(letter.lower())
        else:
            result.append(letter)
    return "".join(result)
main()

