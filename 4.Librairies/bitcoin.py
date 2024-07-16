import sys
import requests


def main():
    if not len(sys.argv) != 2:
        try:
            n= float(sys.argv[1])
            print(n)

        except ValueError:
            sys.exit("ValueError")

        except TypeError:
            sys.exit("TypeError")
    #else:
      #  sys.exit()


#def coindeskapi():
 #   try:

 #   except requests.RequestException:

main()
