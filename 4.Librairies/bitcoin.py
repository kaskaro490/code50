import sys
import requests


def main():

    if not len(sys.argv) != 2:
        try:
            n= float(sys.argv[1])
            print(n)
            coindeskjson = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            for values in

        except requests.RequestException:
            sys.exit("RequestException")

        except ValueError:
            sys.exit("ValueError")

        except TypeError:
            sys.exit("TypeError")

main()
