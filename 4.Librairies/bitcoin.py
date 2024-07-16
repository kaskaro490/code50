import sys
import requests
import json

def main():

    if not len(sys.argv) != 2:
        try:
            n= float(sys.argv[1])
            coindeskjson = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            pythonjson = json.loads(coindeskjson)
            currentprice = pythonjson["bpi"]["USD"]["rate_float"]
            

        except requests.RequestException:
            sys.exit("RequestException")

        except ValueError:
            sys.exit("ValueError")

        except TypeError:
            sys.exit("TypeError")

main()
