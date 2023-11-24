########################################################
# My first Chatbot (Part 1)                       ######
# Auteurs : Aurélien Perez et Titouan Lenain      ######
# Version : V 0.7                                 ######
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

# dictionary of president dictionary based on the current republic
dict_pres = {"p5": {"Macron": "Emmanuel", "Hollande": "François", "Sarkozy": "Nicolas", "Chirac": "Jacques",
                    "Mitterrand": "François", "Giscard dEstaing": "Valéry", "Pompidou": "Georges",
                    "de Gaulle": "Charles"},
             "p4": {"Coty": "René", "Auriol": "Vincent"},
             "p3": {"Lebrun": "Albert", "Doumer": "Paul", "Doumergue": "Gaston", "Millerand": "Alexandre",
                    "Deschanel": "Paul", "Poincaré": "Raymond", "Fallières": "Armand", "Loubet": "Émile",
                    "Faure": "Félix", "Casimir-Perier": "Jean", "Carnot": "Sadi", "Grévy": "Jules",
                    "de Mac Mahon": "Patrice", "Thiers": "Adolphe"}}


# list of punctuation sign
list_punctuation = [
                    '.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '<', '>', "'", '"', '/',
                    '|', '@', '#', '$', '%', '^', '&', '*', '_', '+', '-', '=', '~', '`', "\n"
                    ]

# list of stopword (not important word)
list_stopword = []

########################################################################################################################
# MAIN PROGRAM
########################################################################################################################
# recover the stop words list in the folder
print(list_of_files(directory_base, ".txt"))
with open("stop_words_french.txt", "r") as f1:
    for line in f1:
        list_stopword.append(line[:-1])

name = (extraire_nom(list_files_names))
print(noms_prenoms(dict_pres["p5"], name))
