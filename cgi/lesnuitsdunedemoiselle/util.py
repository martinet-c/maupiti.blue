base_api_url = "http://lesnuitsdunedemoiselle.free.fr/api/"
nb_nights_per_page = 20

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

def print_nights(current_page, data, line_break=False):
    return 0
