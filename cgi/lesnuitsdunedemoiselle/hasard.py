#!/usr/bin/python3
page = "hasard"
import util
util.header(page, "28 nuits au hasard (rafraichissez la page pour 28 nouvelles propositions)")
print("Une des propositions ci-dessous vous plaît ? cliquez-la pour l'aimer et l'ajouter à vos favoris !")
util.print_nights(page, False, True)
util.footer()
