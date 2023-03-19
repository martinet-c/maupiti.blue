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

if data["hash"]:
    import requests
    resp = requests.post("http://lesnuitsdunedemoiselle.free.fr/api/vote.php", data = data)
    if resp.text:
        print("Votre \"j'aime\" n'a malheureusement pas été enregistré :(")
        print("Il y a eu un problème :")
        print("```")
        print(resp.text)
        print("```")
        print("=> /contact.gmi Si vous pensez que cette erreur n'est pas normale, n'hésitez pas à me contacter")
    else:
        print("Votre \"j'aime\" a bien été enregistré !")
else:
    print("Vous aviez déjà aimé cette proposition !")

print("## Vos favoris :")
resp = requests.get("http://lesnuitsdunedemoiselle.free.fr/api/favoris.php?userip=" + environ["REMOTE_ADDR"])
util.print_nights(resp.text)
