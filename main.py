##################################################################
# Name : My first Chatbot (Part 1)                          ######
# Creators : Aurélien Perez & Titouan Lenain (L1 Grp B)     ######
# Version : V 1.0                                           ######
##################################################################

########################################################################################################################
# importing external functions
########################################################################################################################
import os
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
dict_word = dict_words(list_files_path)
for file_path in list_files_path:
    dict_dict_TF[os.path.basename(file_path)] = term_frequency(dict_word, file_path)
dict_idf = inverse_document_frequency(dict_word, dict_dict_TF)
dict_dict_tf_idf = tf_idf(dict_idf, dict_dict_TF)

list_one_to_five = ["1", "2", "3", "4", "5"]

print("Hi. Welcome to this program. What can I do for you ?\n")

while True:
    print("1 - Question types")
    print("2 - Questions globales")
    answer = input()


while answer != 1 or answer != 2:
    if answer == "1":
        answer == -1
        while answer not in list_one_to_five:
            print("1 - Afficher la liste des mots les moins importants dans le corpus de documents.")
            print("2 - Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé.")
            print("3 - Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac, sauf les mots dont le score "
                  "TF-IDF vaut 0.")
            print("4 - Indiquer le(s) nom(s) du/des président(s) qui a/ont parlé de la « Nation ».")
            print("5 - Indiquer le(s) nom(s) du/des président(s) qui a/ont parlé du climat et/ou de l’écologie.")
            answer = input()
            if answer == "1":
                print(q1(dict_dict_tf_idf))
            elif answer == "2":
                print(q2(dict_dict_tf_idf))
            elif answer == "3":
                print(q3())
            elif answer == "4":
                print(q4())
            elif answer == "5":
                print(q5)
    if answer == "2":
        txt_q = input("posez votre question :")
        print(question_global(txt_q, dict_word, dict_idf, dict_dict_tf_idf, directory_base))
    else:
        print("réponse invalide")
    answer = ""

