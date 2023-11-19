from math import log


def extraire_nom(list_names_files):
    list_nom = []
    for i in list_names_files:
        i = i.split("_")[1]
        j = 0
        while 'a' <= i[j] <= 'z' or 'A' <= i[j] <= 'Z' or i[j] == ' ':
            j += 1
        list_nom.append(i[:j])
    return list_nom


def punctuation(nom_dossier, file_name, list_punctuation):
    with open(nom_dossier + file_name, "r") as f1, open("cleaned/" + file_name, "w") as f2:
        text = ""
        for i in f1:
            for j in i:
                if j not in list_punctuation:
                    text += j
                else:
                    text += " "
        text = (" ".join(text.split()))
        f2.write(text)


def stopword(file_name, list_stopword):
    text_c = []
    with open(file_name, "r") as f1:
        text = f1.readline().split()
        for i in text:
            if i not in list_stopword:
                text_c.append(i)
        text_c = (" ".join(text_c))
    with open(file_name, "w") as f1:
        f1.write(text_c)


def minuscule(file_name):
    with open(file_name, "r") as f1:
        txt = f1.readline()
    for i in range(65, 91):
        txt = txt.replace(chr(i), chr(i+32))
    with open(file_name, "w") as f1:
        f1.write(txt)


def term_frequency(txt_cleaned):
    list_txt = txt_cleaned.split(" ")
    set_words = set()
    for i in list_txt:
        set_words.add(i)
    dict_words = dict.fromkeys(set_words, 0)
    for i in list_txt:
        dict_words[i] = dict_words[i]+1
    return dict_words


def inverse_document_frequency(list_dict_term):

    dict_set = set()
    for dict_term in list_dict_term:
        for word in dict_term.keys():
            dict_set.add(word)

    dict_words = dict.fromkeys(dict_set, 0)
    for dict_term in list_dict_term:
        for word in dict_term.keys():
            dict_words[word] = dict_words[word]+1

    nb_documents = len(list_dict_term)
    for i in dict_words:
        dict_words[i] = log(nb_documents/dict_words[i])

    return dict_words

def noms_prenoms(dict_identity,list_name):
    list1=[]
    list_presidents=[]
    for i in dict_identity.items():
        list1.append(dict_identity)
    list_presidents.append(list1)
    return list_presidents