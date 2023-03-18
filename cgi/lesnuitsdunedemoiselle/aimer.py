#!/usr/bin/python3
import util
util.header()
from os import environ
from urllib.parse import parse_qs
data = parse_qs(environ["QUERY_STRING"])
import json
print(json.dumps(data))
data["userip"] = environ["REMOTE_ADDR"]
print(json.dumps(data))
from sys import exit
if "QUERY_STRING" not in environ:
    print("Mauvais paramètres :(")
    exit()
import requests
resp = requests.post("http://lesnuitsdunedemoiselle.free.fr/api/vote.php", data = parse_qs(environ["QUERY_STRING"]))
print(resp.text)
