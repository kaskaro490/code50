import pyfiglet
def main():

    f = pyfiglet.figlet_format(input("Input"), font="sys.argv[2]")
    print(f)

main()
