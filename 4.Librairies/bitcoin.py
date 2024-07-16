import sys
import requests
import json

def main():

    if not len(sys.argv) != 2:
        try:
            n= float(sys.argv[1])
            print("1")
            coindeskjson = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            print("2")
            #pythonjson = json.loads(coindeskjson)
            #print("3")
            currentprice = coindeskjson["bpi"]["USD"]["rate_float"]
            print("4")
            totalcost = currentprice * n
            print("5")
            print(f"${amount:{totalcost},.4f}")


        except requests.RequestException:
            sys.exit("RequestException")

        except ValueError:
            sys.exit("ValueError")

        except TypeError:
            sys.exit("TypeError")

main()
