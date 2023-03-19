base_api_url = "http://lesnuitsdunedemoiselle.free.fr/api/"
nb_nights_per_page = 20

import requests
from os import environ
from urllib.parse import parse_qs

def header(current_page="", alternate_title=""):
    print("20 text/gemini", end="\r\n")
    print("# Les nuits d'une demoiselle ~ générateur de poésie aléatoire")
    pages = {
        "hasard":"28 nuits au hasard",
        "favoris":"Vos meilleures nuits",
        "tendances":"Les meilleures nuits du moment",
        "palmares":"Les meilleures depuis la nuit des temps"
    }
    for page in pages:
        if page != current_page:
            print("=> " + page + ".py " + pages[page])
    if current_page:
        print("## " + (alternate_title if alternate_title else pages[current_page]) + " :")
    print("")

def print_nights(current_page, line_break=False):
    data = parse_qs(environ["QUERY_STRING"])
    url = base_api_url + current_page + ".php?userip=" + environ["REMOTE_ADDR"] + ("&nav=" + data["page"] if "page" in data else "")
    resp = requests.get(url)
    lines = resp.text.splitlines()
    cpt = 0
    for sline in lines:
        line = sline.split(",")
        sentence = line[0]
        nb_votes, last_vote, id_verb, id_noun, hash = "", "", "", "", ""
        if len(line)>1:
            nb_votes = line[1]
            last_vote = line[2]
            if len(line)>3:
                id_verb = line[3]
                id_noun = line[4]
                hash = line[5]
        line = "Je me fais " + sentence
        if nb_votes:
            line += " (" + nb_votes + " j'aime" + (", le dernier il y a " + last_vote if last_vote else "")  + ")"
        if hash:
            line = "=>aimer.py?verb=" + id_verb + "&noun=" + id_noun + "&hash=" + hash + " " + line + " >> cliquez pour aimer"
        else:
            line = "=>aimer.py " + line + " (déjà dans vos favoris)"
        if line_break and cpt%4==0:
            print("")
        print(line)
        cpt+=1
    return cpt

def footer(current_page, nb_nights_in_current_page):
    print("")
    data = parse_qs(environ["QUERY_STRING"])
    page = int(data["page"]) if "page" in data else 1
    url = base_api_url + current_page + ".php?userip=" + environ["REMOTE_ADDR"] + "&nav="
    if page>1:
        print("=> " + url + (page-1) + " page précédente") 
    if nb_nights_in_current_page == nb_nights_per_page:
        print("=> " + url + (page+1) + " page suivante") 
