import os
from Fonctions import*
listnom=os.listdir("speeches-20231116")
prenompres5=["Emmanuel","François","Nicolas","Jacques","François","Valéry","Georges","Charles"]
prenompres4=["René","Vincent"]
prenompres3=["Albert", "Paul", "Gaston", "Alexandre", "Paul", "Raymond", "Armand", "Émile", "Félix", "Jean", "Sadi", "Jules", "Patrice", "Adolphe"]
print(extraire_nom(listnom))

print(ord(' '))
list_ponctuaton = [
    '.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '<', '>', "'", '"', '/',
    '|', '@', '#', '$', '%', '^', '&', '*', '_', '+', '-', '=', '~', '`',"\n"]
listw=[]
with open("speeches-20231116/Nomination_Chirac1.txt","r") as f2, open("chirac123", "w") as f1:
    for i in f2:
        for j in i:
            if j not in list_ponctuaton:
                f1.write(j)
            else:
                f1.write(" ")

with  open("chirac123","r") as f2:
    for i in f2:
        for j in i.split(" "):
            listw.append(j)

print(listw)
#test5