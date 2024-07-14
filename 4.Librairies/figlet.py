from pyfiglet import Figlet
import sys


def argvalid():  # vérifier que les arguments sont valides
    fonts = Figlet().getFonts()
    if 1 < len(sys.argv) < 3:

        if sys.argv[2] not in fonts: # vérifier la longueur des arguments et la validité de la font sys.argv[2]
            return False
        elif sys.argv[1] != "-f":
            return False
        else:
            return True
    else:
        return False

def userfont():
        if sys.argv():
            if argvalid() is True:
                f = Figlet(font = sys.argv[2])
            else:
                sys.exit()

def main():




    user = f.renderText(input('Input: '))
    print(user)






        else:
            f = Figlet(font = 'slant')
        if
            sys.exit()



main()
