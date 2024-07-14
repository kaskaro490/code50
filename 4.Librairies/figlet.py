from pyfiglet import Figlet
import sys
import random


fonts = Figlet().getFonts()


def argvalid():  # vérifier que les arguments sont valides
    if len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font": # vérifier la validité de sys.argv[1] qui doit être -f ou --font
            sys.exit()
        elif sys.argv[2] not in fonts: # vérifier la validité de la font sys.argv[2]
            sys.exit()
        else:
            font = sys.argv[2]
            return font

    elif len(sys.argv) == 0:
        font = random.choice(fonts) #
        return font

    else:
        sys.exit()

def main():

        if argvalid():
            user = input('Input: ')
            print(f.renderText(user))


main()
