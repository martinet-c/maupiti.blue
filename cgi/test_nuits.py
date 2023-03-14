#!/usr/bin/python3
import util
util.header()
import requests
resp = requests.get('http://lesnuitsdunedemoiselle.free.fr/test.php')
print(resp)
