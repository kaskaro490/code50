from pyfiglet import Figlet
import sys


def argvalid():  # vérifier que les arguments sont valides
    fonts = Figlet().getFonts()
    if 1 < len(sys.argv) < 3 and sys.argv[2] in fonts: # vérifier la longueur des arguments et la validité de la font sys.argv[2]
        return True
    else:
        return False

def main():



    if argvalid() is True:
        f = Figlet(font = sys.argv[2])

    else:
        sys.exit()




    user = f.renderText(input('Input: '))
    print(user)






        else:
            f = Figlet(font = 'slant')
        if
            sys.exit()



main()
