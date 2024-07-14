from pyfiglet import Figlet
import sys
import random


fonts = Figlet().getFonts()


def argvalid():  # vérifier que les arguments sont valides
    if sys.argv[2] not in fonts: # vérifier la validité de la font sys.argv[2]
        return sys.exit()
    elif sys.argv[1] != "-f" and sys.argv[1] != "--font": # vérifier la validité de sys.argv[1] qui doit être -f ou --font
        return sys.exit()
    else:
        return True


def userfont():
        if 1 < len(sys.argv) < 4: # Vérifier que le nombre d'arguments et de 3
            if argvalid() is True:
                font = sys.argv[2] # Assigner l'argument 3 à la variable font
                return font
            else:
                return False

        elif len(sys.argv) == 0:
            font = random.choice(fonts) #
            return font
        else:
            sys.exit("bad font argument")
def main():

    if argvalid() is True:
        user = input('Input: ')
        f = Figlet(font=userfont())
        print(f.renderText(user))


main()
