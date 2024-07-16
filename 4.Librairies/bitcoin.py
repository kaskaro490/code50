import sys
import requests
import json


if len(sys.argv) != 2:
    sys.exit()

number_of_bitcoins = sys.argv[1]

