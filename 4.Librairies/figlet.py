from pyfiglet import Figlet
import sys

def main():
    fonts = Figlet().getFonts()

    if 1 < len(sys.argv) <= 2:
        if sys.argv[2] not in fonts:
            sys.exit()
        else:
            f = Figlet(font = sys.argv[2])
    elif:
            f = Figlet(font = 'slant')

    user = f.renderText(input('Input: '))
    print(user)

main()
