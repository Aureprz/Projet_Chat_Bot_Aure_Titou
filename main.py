########################################################
# My first Chatbot (Part 1)                       ######
# Auteurs : Aurélien Perez et Titouan Lenain      ######
# Version : V 1.0                                 ######
########################################################

########################################################################################################################
# importing external functions
########################################################################################################################
# import os
from Fonctions import *

########################################################################################################################
# VARIABLES
########################################################################################################################
# directory containing all the files to analyze
directory_base = os.path.realpath("./speeches-20231116")
directory_clear = os.path.realpath("./cleaned")

# list of file names
list_files_names = list_of_files(directory_base, "txt")

# list of president names
pres_names = list(set(extraire_nom(list_files_names)))

# dictionary of president dictionary based on the current republic
dict_pres = {"p5": {"Macron": "Emmanuel", "Hollande": "François", "Sarkozy": "Nicolas", "Chirac": "Jacques",
                    "Mitterrand": "François", "Giscard dEstaing": "Valéry", "Pompidou": "Georges",
                    "de Gaulle": "Charles"},
             "p4": {"Coty": "René", "Auriol": "Vincent"},
             "p3": {"Lebrun": "Albert", "Doumer": "Paul", "Doumergue": "Gaston", "Millerand": "Alexandre",
                    "Deschanel": "Paul", "Poincaré": "Raymond", "Fallières": "Armand", "Loubet": "Émile",
                    "Faure": "Félix", "Casimir-Perier": "Jean", "Carnot": "Sadi", "Grévy": "Jules",
                    "de Mac Mahon": "Patrice", "Thiers": "Adolphe"}}

#
dict_pres_files = {list_files_names[i]: extraire_nom(list_files_names)[i] for i in range(0, len(list_files_names))}

# dictionaire de dictionaire tf
dict_dict_TF = {}

# list of punctuation sign
list_punctuation = [
                    '.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '<', '>', "'", '"', '/',
                    '|', '@', '#', '$', '%', '^', '&', '*', '_', '+', '-', '=', '~', '`', "\n", "\""
                    ]

# list of stopword (not important word)
list_stopword = []

########################################################################################################################
# MAIN PROGRAM
########################################################################################################################
# recover the stop words list in the folder

with open("stop_words_french.txt", "r", encoding='utf-8') as f1:
    for line in f1:
        list_stopword.append(line[:-1])

# clear files
list_files_path = copy_directory(directory_base, directory_clear)
for i in list_files_path:
    minuscule(i)
    punctuation(i, list_punctuation)

# create TF-IDF
dic_words = dict_words(list_files_path)
for file_path in list_files_path:
    dict_dict_TF[os.path.basename(file_path)] = term_frequency(file_path, dic_words)
dic_if = inverse_document_frequency(dict_dict_TF, dic_words)
TF_IDF = tf_idf(dict_dict_TF, dic_if)


while True:

    print("Hi. Welcome to this program. What can I do for you ?\n")
    print("1. Give you the term frequency of each word in a certain file.")
    print("2. Letting you know the TF-IDF score of each word across the files.")
    print("3. Pick a word and see which president did use it.")
    answer = input()

    if answer == "1":
        while answer != "<":
            print("Choose a president in the dictionary below (name) :")
            dic_pres = noms_prenoms(dict_pres["p5"], pres_names)
            for j in dic_pres:
                print(j, dic_pres[j], end="  ")
            print()
            answer = input()
            if answer != "<":
                name_chosen = answer
                while answer != "<":
                    key_list = [k for (k, val) in dict_pres_files.items() if val == name_chosen]
                    if len(key_list) > 1:
                        print("Be sure to select a specific file :")
                        for i, j in enumerate(key_list):
                            print(i, j, end="  ")
                            print()
                        answer = input()
                        if answer != "<":
                            key_list = key_list[int(answer)]
                    if answer != "<":
                        if answer != ("<" or ""):
                            key_list = "".join(key_list)
                            print(key_list)
                            v = dict_dict_TF[key_list]
                            while answer != "<" or answer < "0":
                                answer = input("Enter a minimal score for the term frequency :")
                                if answer != "<":
                                    for (k, val) in v.items():
                                        if val > int(answer):
                                            print(k + ":", val, end="  ")
                                    print()
                                answer = ""
                            answer = ""
                    answer = ""

        if answer == "2":
            print("By choosing the TF-IDF option, you'll get to know the TF-IDF score across all these files :")
            print(list_files_names)
            print("And here's TF-IDF matrix :")
            print(TF_IDF)

        if answer == "3":
            print(choose_word(dic_words))
            for i in list_files_path:
                if i in dic_words:



