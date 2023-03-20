#!/usr/bin/python3
import util
util.header()
from os import environ
from urllib.parse import parse_qs
data = parse_qs(environ["QUERY_STRING"]) if "QUERY_STRING" in environ else {}
data["userip"] = environ["REMOTE_ADDR"]

if data["hash"]:
    import requests
    resp = requests.post(util.base_api_url + "vote.php", data = data)
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

print("## Vos favoris les plus récents :")
#util.print_nights("favoris", True)
util.footer()
