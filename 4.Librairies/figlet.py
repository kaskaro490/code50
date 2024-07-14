from pyfiglet import Figlet
import sys


def valid():  # vérifier que les arguments sont valides
    if 1 < len(sys.argv) < 3 and sys.argv[2] is in fonts:
            return True
    else:
         return False

def main():
    fonts = Figlet().getFonts()



        # vérifier la longueur des arguments
        # vérifier que sys.argv[2] est une font valide








    if 1 < len(sys.argv) < 2 and sys.argv[2] not in fonts:
        if
            sys.exit()
        if:
            f = Figlet(font = sys.argv[2])
        else:
            f = Figlet(font = 'slant')

    user = f.renderText(input('Input: '))
    print(user)

main()
