#!/usr/bin/python3
import util
util.header("palmares")
import requests
resp = requests.get("http://lesnuitsdunedemoiselle.free.fr/api/palmares.php")
util.print_nights(resp.text)
