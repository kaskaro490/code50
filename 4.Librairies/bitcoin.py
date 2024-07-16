import sys
import requests


def main():
    n = getnum()
    print(n)

def getnum():
    if len(sys.argv) != 2:
        sys.exit()
    else:
        n = sys.argv[1]
        return n


#def coindeskapi():
 #   try:

 #   except requests.RequestException:

