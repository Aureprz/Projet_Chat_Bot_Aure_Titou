def extraire_nom(list):
    list_nom=[]
    for i in list:
        i = i.split("_")[1]
        j=0
        while 'z'>=i[j] and i[j]>='a' or 'Z'>=i[j] and i[j]>='A' or i[j]==' ':
            j+=1
        list_nom.append(i[:j])
    return(list_nom)


def TF(txt_cleaned):
    list = txt_cleaned.split(" ")
    set_words = set()
    dict_words = {}
    for i in list:
        set_words.add(i)
    dict_words = dict.fromkeys(set_words, 0)
    for i in list:
       dict_words[i] = dict_words[i]+1
    return dict_words


def noms_prenoms(list,dict):
    prenompres5 = ["Emmanuel", "François", "Nicolas", "Jacques", "François", "Valéry", "Georges", "Charles"]
    #nom en clé, prenom en valeur
    for i in len(prenompres5):
