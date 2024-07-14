from pyfiglet import Figlet
import sys


def valid():  # vérifier que les arguments sont valides
    fonts = Figlet().getFonts()
    if 1 < len(sys.argv) < 3 and sys.argv[2] in fonts: # vérifier la longueur des arguments et la validité de la font sys.argv[2]
        return True
    else:
        return False

def main():



    if
        f = Figlet(font = sys.argv[2])




    user = f.renderText(input('Input: '))
    print(user)




    if 1 < len(sys.argv) < 2 and sys.argv[2] not in fonts:

        if:

        else:
            f = Figlet(font = 'slant')
        if
            sys.exit()



main()
