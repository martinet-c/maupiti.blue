def header(current_page="", alternate_title=""):
    print("20 text/gemini", end="\r\n")
    print("# Les nuits d'une demoiselle ~ générateur de poésie aléatoire")
    pages = {"hasard":"28 nuits au hasard", "favoris":"vos meilleures nuits", "tendances":"les meilleures nuits du moment", "palmares":"depuis la nuit des temps"}
    for page in pages:
        if page != current_page:
            print("=> " + page + ".py " + pages[page])
    if current_page:
        print("## " + (alternate_title if alternate_title else pages[current_page]))
    print("")

def print_nights(resp_text, line_break=False):
    lines = resp_text.splitlines()
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
