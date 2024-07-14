from pyfiglet import Figlet
import sys

def main():
    if 1 < len(sys.argv) <= 2:

        fonts = Figlet().getFonts()
        if sys.argv[2] not in fonts:
            f = Figlet(font = sys.argv[2])
        else:
            sys.exit()
    elif:
            f = Figlet(font = 'slant')

    user = f.renderText(input('Input: '))
    print(user)

main()
