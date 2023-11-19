import os
from Fonctions import*
name_list = os.listdir("speeches-20231116")
dict_pres5 = {"Macron": "Emmanuel", "Hollande": "François", "Sarkozy": "Nicolas", "Chirac": "Jacques",
              "Mitterrand": "François", "Giscard dEstaing": "Valéry", "Pompidou": "Georges",
              "de Gaulle": "Charles"}
prenompres4 = ["René", "Vincent"]
prenompres3 = ["Albert", "Paul", "Gaston", "Alexandre", "Paul", "Raymond", "Armand", "Émile", "Félix", "Jean", "Sadi",
               "Jules", "Patrice", "Adolphe"]
print(extraire_nom(name_list))

list_punctuation = [
    '.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '<', '>', "'", '"', '/',
    '|', '@', '#', '$', '%', '^', '&', '*', '_', '+', '-', '=', '~', '`', "\n"]
list_stopword = []

with open("stop_words_french.txt", "r") as f1:
    for line in f1:
        list_stopword.append(line[:-1])

punctuation("speeches-20231116", "/Nomination_Chirac1.txt", list_punctuation)
minuscule("cleaned/Nomination_Chirac1.txt")
stopword("cleaned/Nomination_Chirac1.txt", list_stopword)
