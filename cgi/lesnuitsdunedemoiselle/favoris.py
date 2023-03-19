#!/usr/bin/python3
page = "favoris"
import util
util.header(page)
cpt = util.print_nights(page)
if cpt==0:
    print("Vous n'avez pas encore de favoris, c'est triste :(")
    print("Cliquez sur les propositions que vous aimez sur les autres pages !")
else:
    util.footer(page, cpt)
