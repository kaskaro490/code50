from pyfiglet import Figlet
import sys

def main():
    if 1 < len(sys.argv) <= 2:

        fonts = Figlet().getFonts()
        if argv[2] not in fonts:
            f = Figlet(font = sys.argv[2])
        elif:
            f = Figlet(font = 'slant')
        else:
            sys.exit()

    user = f.renderText(input('Input: '))
    print(user)

main()
