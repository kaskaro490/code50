from pyfiglet import Figlet
import sys

def main():
    if len(sys.argv) > 1:
        f = Figlet(font = sys.argv[2])
    else:
        f = Figlet(font = 'slant')

    user = f.renderText(input('Input: '))
    print(user)

main()
