from pyfiglet import Figlet
import sys

def main():
    if 1 < len(sys.argv) <= 2:

        if 
            f = Figlet(font = sys.argv[2])
        elif:
            f = Figlet(font = 'slant')
        else:
            sys.exit()

    user = f.renderText(input('Input: '))
    print(user)

main()
