#!/usr/bin/python3
import util
util.header("tendances")
import requests
resp = requests.get("http://lesnuitsdunedemoiselle.free.fr/api/tendances.php")
util.print_nights(resp.text)
