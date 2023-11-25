########################################################
# My first Chatbot (Part 1)                       ######
# Auteurs : Aurélien Perez et Titouan Lenain      ######
# Version : V 0.8                                 ######
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
pres_names = extraire_nom(list_files_names)

# dictionary of president dictionary based on the current republic
dict_pres = {"p5": {"Macron": "Emmanuel", "Hollande": "François", "Sarkozy": "Nicolas", "Chirac": "Jacques",
                    "Mitterrand": "François", "Giscard dEstaing": "Valéry", "Pompidou": "Georges",
                    "de Gaulle": "Charles"},
             "p4": {"Coty": "René", "Auriol": "Vincent"},
             "p3": {"Lebrun": "Albert", "Doumer": "Paul", "Doumergue": "Gaston", "Millerand": "Alexandre",
                    "Deschanel": "Paul", "Poincaré": "Raymond", "Fallières": "Armand", "Loubet": "Émile",
                    "Faure": "Félix", "Casimir-Perier": "Jean", "Carnot": "Sadi", "Grévy": "Jules",
                    "de Mac Mahon": "Patrice", "Thiers": "Adolphe"}}

# dictionaire de dictionaire tf
dict_dict_TF = {}

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


with open("stop_words_french.txt", "r") as f1:
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
    dict_dict_TF[file_path] = term_frequency(file_path, dic_words)
dic_if = inverse_document_frequency(dict_dict_TF, dic_words)
TF_IDF = tf_idf(dict_dict_TF, dic_if)

N = -1
while (N > 9) or (N < 0):
    print("Hi. Welcome to this program. What can I do for you ?")
    print("1. Give you the term frequency of each word in a certain file.")
    print("2. Letting you know the words a president use a lot.")
    print("3. Which words every president in this list use ?")
    N = int(input())

if N == 1:
    print("Choose a president in the dictionary below (number) :")
    dic_pres = noms_prenoms(dict_pres["p5"], pres_names)
    for i, j in enumerate(dic_pres):
        print(i, j, dic_pres[j], end="  ")
    input()
