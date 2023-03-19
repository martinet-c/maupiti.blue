#!/usr/bin/python3
import util
util.header("palmares")
from os import environ
import requests
resp = requests.get("http://lesnuitsdunedemoiselle.free.fr/api/palmares.php" + environ["REMOTE_ADDR"])
util.print_nights(resp.text)
