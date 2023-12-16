##################################################################
# Name : My first Chatbot (Part 1)                          ######
# Creators : Aurélien Perez & Titouan Lenain (L1 Grp B)     ######
# Version : V 1.0                                           ######
##################################################################

########################################################################################################################
# importing external functions
########################################################################################################################
# import os
from Fonctions import *
from tf_idf import *
from FunctionsPart1 import *
########################################################################################################################
# VARIABLES
########################################################################################################################
# directory containing all the files to analyze
directory_base = os.path.realpath("speeches-20231116")
directory_clear = os.path.realpath("cleaned")

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


########################################################################################################################
# MAIN PROGRAM
########################################################################################################################

# clear files
list_files_path = copy_directory(directory_base, directory_clear)
for i in list_files_path:
    text = file_to_str(i)
    text = clean(text)
    str_to_file(text, i)
# create TF-IDF
dic_words = dict_words(list_files_path)
for file_path in list_files_path:
    dict_dict_TF[os.path.basename(file_path)] = term_frequency(dic_words, file_path)
dict_idf = inverse_document_frequency(dic_words, dict_dict_TF)
dict_dict_tf_idf = tf_idf(dict_idf, dict_dict_TF)


print("Hi. Welcome to this program. What can I do for you ?\n")

while True:
    print("0. Settings")
    print("1. Select a type of value")
    answer = input()

    if answer == "1":
        print("noting")
    else:
        print("Answer not defined.")
