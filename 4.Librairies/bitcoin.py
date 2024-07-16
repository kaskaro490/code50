import sys
import requests


def main():
    numbit = getnum()
    print(numbit)

def getnum():
    if len(sys.argv) != 2:
        sys.exit()
    else:
        numbit = sys.argv[1]


#def coindeskapi():
 #   try:

 #   except requests.RequestException:

