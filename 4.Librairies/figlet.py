import pyfiglet
import sys

def main():
    if len(sys.argv) > 1:
        argfont = sys.argv[2]
    else:
        argfont = ""

    f = pyfiglet.figlet_format(input("Input: "), font=argfont)
    print(f)

main()
