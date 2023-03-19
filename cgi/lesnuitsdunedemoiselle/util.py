def header():
    print("20 text/gemini", end="\r\n")

def print_nights(resp, line_break=False):
    lines = (resp.text).splitlines()
    cpt = 0
    for sline in lines:
        line = sline.split(",")
        sentence = line[0]
        if len(line)>1:
            nb_votes = line[1]
            last_vote = line[2]
            if len(line)>3:
                id_verb = line[3]
                id_noun = line[4]
                hash = line[5]
        line = "Je me fais " + sentence
        #if nb_votes:
            #line += " (" + nb_votes + " j'aime" + (last_vote if ", le dernier il y a " + last_vote else "")  + ")"
        if hash:
            line = "=>aimer.py?verb=" + id_verb + "&noun=" + id_noun + "&hash=" + hash + " " + line + " >> cliquez pour aimer"
        if line_break and cpt%4==0:
            print("")
        print(line)
        cpt+=1
