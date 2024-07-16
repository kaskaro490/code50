import sys
import requests


def main():
    getnum()
    numbit = sys.argv[1]
    print(numbit)

def getnum():
    if len(sys.argv) != 2:
        sys.exit()
    else:

        return numbit


#def coindeskapi():
 #   try:

 #   except requests.RequestException:

