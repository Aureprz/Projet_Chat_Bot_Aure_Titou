
import os
"""
Dossier qui regroupe l'ensemble des fonctions général
"""

def extraire_nom(list_names_files) -> list:
    """
    fonction pour extraire le nom de chaque fichier (discours)
    :param list_names_files: liste des noms de chaque fichier
    :return: liste des noms des président
    """
    list_nom = []
    for file_name in list_names_files:
        # Remove "Nomination_" and ".txt"
        name = file_name.split("_")[1].split(".txt")[0]
        j = len(name)-1
        while not (name[j].isalpha() or name[j].isspace()):
            j -= 1
        list_nom.append(name[:j+1])
    # Return a list of "cleaned" files name
    return list(list_nom)


def noms_prenoms(dict_identity, list_noms) -> dict:
    """
    fonction donnant la liste des noms et prénoms associés à chaque président
    :param dict_identity: dictionnaire qui répertorie les noms des présidents et les prénoms associés
    :param list_noms: liste des noms des présidents qui ont parlé
    :return: dictionnaire qui liste les noms et les prénoms des président dans le corpus
    """
    dict_presidents = {i: dict_identity[i] for i in list_noms}
    return dict_presidents


def list_of_files(directory, extension) -> list:
    """
    fonction qui renvoie chaque nom de fichier entièrement sous la forme d’une liste
    :param directory: dossier des fichiers
    :param extension: extension des fichiers
    :return: liste des noms de fichiers
    """
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def copy_directory(directory1, directory2) -> list:
    """
    Cette fonction permet de copier les fichiers d'un dossier vers un autre dossier
    :param directory1: dossier de départ
    :param directory2: dossier d'arrivée
    :return: list des chemins des fichiers dans le dossier d'arrivée
    """
    list_directory2 = []
    for files in os.listdir(directory1):
        with open(os.path.join(directory1, files), "r", encoding='utf-8') as f1, open(os.path.join(directory2, files),
                                                                                      "w", encoding='utf-8') as f2:
            f2.write(f1.read())
        list_directory2.append(os.path.join(directory2, files))
    return list_directory2


def dict_words(list_path_files) -> dict:
    """
    fonction qui renvoie un dictionnaire de chaque mot du corpus, en une seule copie, avec une valeur nulle
    :param list_path_files: chemins des fichiers dans le corpus
    :return: dictionnaire des mots du corpus
    """
    list_txt = []
    for path_files in list_path_files:
        txt = file_to_str(path_files)
        list_txt += txt.split()
    set_words = set(list_txt)
    dict_word = dict.fromkeys(set_words, 0)
    return dict_word


def deref_dic_dic(dic_dic) -> dict:
    """
    la fonction qui permet de déréférencer les adresses un dictionnaire
    :param dic_dic: dictionnaire de dictionnaires mal référencer
    :return: un dictionnaire de dictionnaires avec les même valeurs
    """
    dic_dic_2 = {}
    for dic in dic_dic:
        dic_dic_2[dic] = {}
        for k, val in dic_dic[dic].items():
            dic_dic_2[dic][k] = val
    return dic_dic_2


def deref_dic_key(dic) -> list:
    """
    la fonction qui permet de déréférencer les clefs d'un dictionnaire
    :param dic: dictionnaire mal référencer
    :return: list des clefs du dictionnaire
    """
    list_key = []
    for k in dic.keys():
        list_key.append(k)
    return list_key


def func_sort(dic, type_sort) -> dict:
    """
    Trier les valeurs d'un dictionnaire
    :param dic:
    :param type_sort: type de trie si type_sort=True ordre décroissant et si type_sort=False ordre croissant
    :return: renvoi un dictionnaire trié
    """
    dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=type_sort))
    return dic


def f_mean(dic_dic) -> dict:
    """
    Donne la moyenne de toutes les valeurs selon le mot (s) choisi et le type de résultat sélectionné
    :param dic_dic: dictionnaire de dictionnaires de mots associés à des valeurs numériques
    :return: renvoie la valeur moyenne de toutes les valeurs pour un mot donné
    """
    dico = {}
    nb_doc = len(dic_dic)
    for name in dic_dic:
        for word, val in dic_dic[name].items():
            if word in dico:
                dico[word] += val
            else:
                dico[word] = val
    for word, val in dico.items():
        dico[word] /= nb_doc
    return dico


def file_to_str(file_path) -> str:
    """
    Cette fonction lit un fichier et récupère son contenu
    :param file_path: chemin d'accès du fichier
    :return: contenu du fichier en str
    """
    with open(file_path, "r", encoding='utf-8') as f1:
        txt = f1.read()
    return txt


def str_to_file(chaine, file_path):
    """
    Cette fonction écrit un texte dans un fichier
    :param chaine: texte à écrire dans le fichier
    :param file_path: chemin du fichier
    :return: Rien
    """
    with open(file_path, "w", encoding='utf-8') as f1:
        f1.write(chaine)


def equivalent_str(name_file, path_directory):
    """
    Cette fonction permet de recupperer le text d'un fichier dans un dossier
    :param name_file: nom du fichier
    :param path_directory: chemin du dossier
    :return: texte du fichier dans le dossier
    """
    path_file = os.path.join(path_directory, name_file,)
    text = file_to_str(path_file)
    return text


def count_word(file_path):
    """
    Cette fonction compte le nombre de mots dans un fichier
    :param file_path: chemin du fichier
    :return: nombre de mots dans un fichier
    """
    text = file_to_str(file_path)
    nb_word = len(text.split())
    return nb_word

if __name__ == "__main__":
    print("Do not run this file.")
    print("Run ./main.py")
