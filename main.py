########################################################
# Name : My first Chatbot (Part 1)                ######
# Auteurs : Aurélien Perez & Titouan Lenain       ######
# Version : V 1.0                                 ######
########################################################

########################################################################################################################
# importing external functions
########################################################################################################################
# import os
from Fonctions import *
from Menu import *
from tf_idf import *
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
word = deref_dic_key(dic_words)
files = list_files_names
interval = [0, 100]
decimal = 3
show_val = True
type_sort = True
mean = True
print("Hi. Welcome to this program. What can I do for you ?\n")

while True:
    print("0. Settings")
    print("1. Select a type of value")
    print("2. Select a file")
    print("3. Pick a word")
    print("4. Pick an interval")
    print("5. select a type of sort")
    print("6. mean on/off")
    print("7. nb of decimal")
    print("8. val on/off")
    print("9. Reply result")
    answer = input()

    if answer == "1":
        type_value = choose_type()
    elif answer == "0":
        if word == deref_dic_key(dic_words):
            word_p = ["%all%"]
        else:
            word_p = word
        if files == list_files_names:
            files_p = ["%all%"]
        else:
            files_p = files
        if type_sort is False:
            type_sort_p = "[ascending]"
        else:
            type_sort_p = "[descending]"
        if mean is False:
            mean_p = "[OFF]"
        else:
            mean_p = "[ON]"
        if show_val is False:
            show_val_p = "[OFF]"
        else:
            show_val_p = "[ON]"
        print("type_value= [" + type_value + "]\nfile=", files_p, "\nword=", word_p, "\ninterval=", interval,
              "\nsort=", type_sort_p, "\nmean=", mean_p, "\ndecimal= [" + str(decimal) + "]\nvalue=", show_val_p,
              "\n" * 2)
    elif answer == "2":
        files = choose_file(dict_pres, pres_names, dict_pres_files, list_files_names)
    elif answer == "3":
        word = choose_word(dic_words)
    elif answer == "4":
        interval = choose_interval()
    elif answer == "5":
        type_sort = choose_sort()
    elif answer == "6":
        mean = choose_mean()
    elif answer == "7":
        decimal = choose_decimal()
    elif answer == "8":
        show_val = choose_show_val()
    elif answer == "9":
        reply(type_value, word, files, dict_dict_TF, dic_if, TF_IDF, interval, type_sort, mean, decimal, show_val)
    else:
        print("Answer not defined.")
    answer = ""
