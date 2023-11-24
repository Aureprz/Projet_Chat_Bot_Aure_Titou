from math import log10
import os


# function to extract the name of each file (speech)
def extraire_nom(list_names_files):
    list_nom = set()
    for file_name in list_names_files:
        # Remove "Nomination_" et ".txt"
        name = file_name.split("_")[1].split(".txt")[0]
        j = len(name)-1
        while not (name[j].isalpha() or name[j].isspace()):
            j -= 1
        list_nom.add(name[:j+1])
    return list(list_nom)


# function removing each punctuation element, such as commas or hyphens, from files
def punctuation(starting_directory, end_directory, file_name, list_punctuation):
    with open(starting_directory + file_name, "r") as f1, open(end_directory + file_name, "w") as f2:
        text = f1.read()
        for char in list_punctuation:
            text = text.replace(char, " ")
        text = " ".join(text.split())
        f2.write(text)


# function to remove words that appear too often (defined by a predefined list)
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


# function transforming the text of each file into lowercase letters
def minuscule(file_name):
    with open(file_name, "r") as f1:
        txt = f1.read()
    translation_table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")
    txt = txt.translate(translation_table)
    with open(file_name, "w") as f1:
        f1.write(txt)


# TF function calculating the frequency of occurrence of a term in such file
def term_frequency(txt_cleaned):
    list_txt = txt_cleaned.split(" ")
    set_words = set()
    for i in list_txt:
        set_words.add(i)

    dict_words = dict.fromkeys(set_words, 0)
    for i in list_txt:
        dict_words[i] = dict_words[i]+1
    return dict_words


# IDF function calculating the importance of a term across all existing files
def inverse_document_frequency(list_dict_term):
    dict_set = set()
    for dict_term in list_dict_term:
        for word in dict_term.keys():
            dict_set.add(word)

    dict_words = dict.fromkeys(dict_set, 0)
    for dict_term in list_dict_term:
        for word in dict_term.keys():
            dict_words[word] = dict_words[word] + 1

    nb_documents = len(list_dict_term)
    for i in dict_words:
        dict_words[i] = log10((nb_documents / dict_words[i])+1)

    return dict_words


# function giving the list of first and last names associated with each president
def noms_prenoms(dict_identity, list_noms):
    dict_presidents = {i: dict_identity[i] for i in list_noms}
    return dict_presidents


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


# verifier tf_idf
def tf_idf(dic_tf, idf):
    dic_tf_idf = {i: {j: dic_tf[i][j] * idf[j] for j in dic_tf[i].keys()} for i in dic_tf.keys()}
    return dic_tf_idf
