#!/usr/bin/python3
import util
util.header()
from urllib.parse import unquote
from os import environ
print(environ["REMOTE_ADDR"])
from sys import exit
if "QUERY_STRING" not in environ:
    print("Mauvais paramètres :(")
    exit()
from urllib.parse import parse_qs
import requests
resp = requests.post("http://lesnuitsdunedemoiselle.free.fr/api/vote.php", data = parse_qs(environ["QUERY_STRING"]))
print(resp.text)
