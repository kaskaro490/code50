import pyfiglet
import sys

def main():
    if sys.argv[2]:
        argfont = sys.argv[2]
    else:
        argfont = None

    f = pyfiglet.figlet_format(input("Input: "), font=argfont)
    print(f)

main()
