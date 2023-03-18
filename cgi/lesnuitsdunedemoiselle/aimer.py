#!/usr/bin/python3
import util
util.header()
from os import environ
from sys import exit
if "QUERY_STRING" not in environ:
    print("Mauvais paramètres :(")
    exit()
from urllib.parse import parse_qs
data = parse_qs(environ["QUERY_STRING"])
data["userip"] = environ["REMOTE_ADDR"]
import requests
resp = requests.post("http://lesnuitsdunedemoiselle.free.fr/api/vote.php", data = data)
print(resp.text)
