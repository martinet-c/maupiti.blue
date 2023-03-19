#!/usr/bin/python3
import util
util.header("favoris")
import requests
from os import environ
resp = requests.get("http://lesnuitsdunedemoiselle.free.fr/api/favoris.php?userip=" + environ["REMOTE_ADDR"])
util.print_nights(resp.text)
