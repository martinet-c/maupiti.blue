#!/usr/bin/python3
import util
util.header()
from os import environ
from sys import exit
if "QUERY_STRING" not in environ:
    print("Mauvais paramètres :(")
    exit()
from urllib.parse import parse_qs
data = parse_qs(environ["QUERY_STRING"])
data["userip"] = environ["REMOTE_ADDR"]
import requests
resp = requests.post("http://lesnuitsdunedemoiselle.free.fr/api/vote.php", data = data)

if resp.text:
    print("Votre \"j'aime\" n'a malheureusement pas été enregistré :(")
    print("Il y a eu une problème :")
    print("```")
    print(resp.text)
    print("```")
    print("Si vous pensez que cette erreur n'est pas normale,")
    print("=> /contact.gmi n'hésitez pas à me contacter")
else:
    print("Votre \"j'aime\" a bien été enregistré !")

print("## Vos favoris :")
resp = requests.get("http://lesnuitsdunedemoiselle.free.fr/api/favoris.php")
util.print_nights(resp)
