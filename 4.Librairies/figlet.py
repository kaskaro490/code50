from pyfiglet import Figlet
import sys
import random


fonts = Figlet().getFonts()


def argvalid():  # vérifier que les arguments sont valides
    if len(sys.argv) == 3:
        

def main():

    if argvalid() is True:
        user = input('Input: ')
        print(f.renderText(user))


main()
