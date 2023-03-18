#!/usr/bin/python3
import util
util.header()

import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print('IP Address:{}'.format(ip_address))

from urllib.parse import unquote
from os import environ
from sys import exit
if "QUERY_STRING" not in environ:
    print("Mauvais paramètres :(")
    exit()
from urllib.parse import parse_qs
import requests
resp = requests.post("http://lesnuitsdunedemoiselle.free.fr/api/vote.php", data = parse_qs(environ["QUERY_STRING"]))
print(resp.text)
