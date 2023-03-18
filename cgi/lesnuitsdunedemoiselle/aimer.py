#!/usr/bin/python3
import util
util.header()
from urllib.parse import unquote
from os import environ
from sys import exit
if "QUERY_STRING" not in environ:
    print("Mauvais paramètres :(")
    exit()
import json
from urllib.parse import parse_qs
print(json.dumps(parse_qs(environ["QUERY_STRING"])))

#params = unquote(environ["QUERY_STRING"]).split("&")
#jparams = "{"
#for sparam in params:
#    param = sparam.split("=")
#    jparams += '"' + param[0] + '":"' + param[1] + '", '
#jparams = jparams[0:len(jparams)-2] + "}"
#print(jparams)
#import requests
#resp = requests.post("http://lesnuitsdunedemoiselle.free.fr/api/vote.php", json = jparams)
#print(resp.text)
