base_api_url = "http://lesnuitsdunedemoiselle.free.fr/api/"
nb_nights_per_page = 20

from os import environ
from urllib.parse import parse_qs

def footer(current_page="", nb_nights_in_current_page=0):
    if current_page and nb_nights_in_current_page:
        print("")
        data = parse_qs(environ["QUERY_STRING"]) if "QUERY_STRING" in environ else {}
        page = int(data["page"]) if "page" in data else 1
        if page>1:
            print("=> " + current_page + ".py?page=" + str(page-1) + " << page précédente") 
        if nb_nights_in_current_page == nb_nights_per_page:
            print("=> " + current_page + ".py?page=" + str(page+1) + " >> page suivante") 
    print("")
    print("Mots issus de lexique.org : 6 400 verbes, 31 000 noms, 198 millions de possibilités")
