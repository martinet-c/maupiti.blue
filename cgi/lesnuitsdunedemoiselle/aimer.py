#!/usr/bin/python3
import util
util.header()
from urllib.parse import unquote
from os import environ
from sys import exit
if "QUERY_STRING" not in environ:
    print("Mauvais paramètres :(")
params = unquote(environ["QUERY_STRING"])
print(params)
