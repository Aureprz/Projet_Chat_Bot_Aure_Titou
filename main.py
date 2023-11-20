import os
from Fonctions import*
directory = "./speeches-20231116"
files_names = list_of_files(directory, "txt")
dict_pres5 = {"Macron": "Emmanuel", "Hollande": "François", "Sarkozy": "Nicolas", "Chirac": "Jacques",
              "Mitterrand": "François", "Giscard dEstaing": "Valéry", "Pompidou": "Georges",
              "de Gaulle": "Charles"}
prenompres4 = {"Coty": "René", "Auriol": "Vincent"}
prenompres3 = {"Lebrun": "Albert", "Doumer": "Paul", "Doumergue": "Gaston", "Millerand": "Alexandre", "Deschanel": "Paul", "Poincaré": "Raymond", "Fallières": "Armand", "Loubet": "Émile", "Faure": "Félix", "Casimir-Perier": "Jean", "Carnot": "Sadi",
               "Grévy": "Jules", "de Mac Mahon": "Patrice", "Thiers": "Adolphe"}
list_punctuation = [
    '.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '<', '>', "'", '"', '/',
    '|', '@', '#', '$', '%', '^', '&', '*', '_', '+', '-', '=', '~', '`', "\n"]
list_stopword = []
print(files_names)
#recupère la list_stopword
with open("stop_words_french.txt", "r") as f1:
    for line in f1:
        list_stopword.append(line[:-1])

punctuation("./speeches-20231116", "./cleaned", "/Nomination_Chirac1.txt", list_punctuation)
minuscule("cleaned/Nomination_Chirac1.txt")
stopword("cleaned/Nomination_Chirac1.txt", list_stopword)
