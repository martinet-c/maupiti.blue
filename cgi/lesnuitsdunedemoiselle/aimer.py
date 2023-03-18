#!/usr/bin/python3
import util
util.header()
from urllib.parse import unquote
from os import environ
from sys import exit
if "QUERY_STRING" not in environ:
    print("Mauvais paramètres :(")
    exit()
params = unquote(environ["QUERY_STRING"]).split("&")
json = "{"
for sparam in params:
    param = sparam.split("=")
    json += '"' + param[0] + '":"' + param[1] + '", '
json = json[0, len(json)] + "}"
print(json)
