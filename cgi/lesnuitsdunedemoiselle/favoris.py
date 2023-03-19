#!/usr/bin/python3
import util
util.header("favoris")
import requests
from os import environ
resp = requests.get("http://lesnuitsdunedemoiselle.free.fr/api/favoris.php?userip=" + environ["REMOTE_ADDR"])
cpt = util.print_nights(resp.text)
if cpt==0:
    print("Vous n'avez pas encore de favoris, c'est triste :(")
    print("Cliquez sur les propositions que vous aimez sur les autres pages !")
