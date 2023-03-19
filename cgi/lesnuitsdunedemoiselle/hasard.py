#!/usr/bin/python3
import util
util.header("hasard", "28 nuits au hasard (rafraichissez la page pour 28 nouvelles propositions)")
print("Vous aimez une des propositions ci-dessous ? cliquez dessus pour l'aimer et l'ajouter à vos favoris !")
import requests
resp = requests.get("http://lesnuitsdunedemoiselle.free.fr/api/hasard.php")
util.print_nights(resp.text, True)
