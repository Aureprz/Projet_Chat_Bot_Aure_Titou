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

#
type_value = "tf"
word = dic_words.keys()
files = list_files_names
interval = [0, 100]

print("Hi. Welcome to this program. What can I do for you ?\n")
while True:

    print("1. select type of value")
    print("2. select a files")
    print("3. select a word")
    print("4. select a interval")
    print("5. reply result")
    answer = input()

    if answer == "1":
        type_value = choose_type()
    if answer == "2":
        files = choose_file(dict_pres, pres_names, dict_pres_files, list_files_names)
    if answer == "3":
        word = choose_word(dic_words)
    if answer == "4":
        interval = choose_interval()
    if answer == "5":
        reponse(type_value, word, files, dict_dict_TF, dic_if, TF_IDF, interval)
    else:
        print("answer undefined")
    answer = ""



