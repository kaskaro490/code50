from pyfiglet import Figlet
import sys


def argvalid():  # vérifier que les arguments sont valides
    fonts = Figlet().getFonts()
    if sys.argv[2] not in fonts: # vérifier la validité de la font sys.argv[2]
        return False
    #if sys.argv[1] != "-f" and sys.argv[1] != "--font": # vérifier la validité de sys.argv[1] qui doit être -f ou --font
       # return False
    else:
        return True


def userfont():
        if 1 < len(sys.argv) < 3:
            print("len ok")
            if argvalid() is True:
                print("argvalid() is True")
                font = sys.argv[2]
            else:
                sys.exit("bad font argument")
        else:
            font = "3x5"
            return font

def main():

    #user = input('Input: ')
    f = Figlet(font=userfont())
    print(f.renderText('text to render'))





main()
