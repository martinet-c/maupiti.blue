#!/usr/bin/python3
import util
util.header("tendances")
from os import environ
import requests
resp = requests.get("http://lesnuitsdunedemoiselle.free.fr/api/tendances.php" + environ["REMOTE_ADDR"])
util.print_nights(resp.text)
