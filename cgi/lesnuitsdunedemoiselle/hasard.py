#!/usr/bin/python3
import util
util.header()
import requests
resp = requests.get('http://lesnuitsdunedemoiselle.free.fr/api/hasard.php')
lines = (resp.text).splitlines()
cpt = 0
for sline in lines:
    line = sline.split(',')
    sentence = line[0]
    if len(line)>1:
        nb_votes = line[1]
        last_vote = line[2]
        if len(line)>3:
            id_verb = line[3]
            id_noun = line[4]
            hash = line[5]
    line = "Je me fais " + sentence
    if cpt%4==0:
        print('')
    print(line)
    cpt+=1