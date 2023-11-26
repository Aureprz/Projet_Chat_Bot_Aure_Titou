from math import log10
import os


def extraire_nom(list_names_files):
    """function to extract the name of each file (speech)"""
    list_nom = []
    for file_name in list_names_files:
        # Remove "Nomination_" et ".txt"
        name = file_name.split("_")[1].split(".txt")[0]
        j = len(name)-1
        while not (name[j].isalpha() or name[j].isspace()):
            j -= 1
        list_nom.append(name[:j+1])
    return list(list_nom)


def punctuation(file_path, list_punctuation):
    """ function removing each punctuation element, such as commas or hyphens, from files"""
    list_punctuation = "".join(list_punctuation)
    with open(file_path, "r", encoding='utf-8') as f1:
        txt = f1.read()
        translation_table = str.maketrans(list_punctuation, " " * len(list_punctuation))
        txt = txt.translate(translation_table)
        txt = " ".join(txt.split())

    with open(file_path, "w", encoding='utf-8') as f1:
        f1.write(txt)


def stopword(file_path, list_stopword):
    """function to remove words that appear too often (defined by a predefined list)"""
    text_c = []
    with open(file_path, "r", encoding='utf-8') as f1:
        text = f1.readline().split()
        text_c = " ".join(word for word in text if word not in list_stopword)
    with open(file_path, "w", encoding='utf-8') as f1:
        f1.write(text_c)


def minuscule(file_path):
    """function transforming the text of each file into lowercase letters"""
    with open(file_path, "r", encoding='utf-8') as f1:
        txt = f1.read()
    translation_table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")
    txt = txt.translate(translation_table)
    with open(file_path, "w", encoding='utf-8') as f1:
        f1.write(txt)


def term_frequency(name_file_cleaned, dict_word):
    """TF function calculating the frequency of occurrence of a term in such file"""
    score_tf = dict_word.copy()
    with open(name_file_cleaned, "r", encoding='utf-8') as f1:
        list_txt = f1.read().split(" ")
    for i in list_txt:
        score_tf[i] = score_tf[i]+1
    return score_tf


def inverse_document_frequency(list_dict_term, dict_word):
    """IDF function calculating the importance of a term across all existing files"""
    score_tf = dict_word.copy()
    for dict_term in list_dict_term.values():
        for word in dict_term.keys():
            if dict_term[word] > 0:
                score_tf[word] = score_tf[word] + 1

    nb_documents = len(list_dict_term)
    for i in score_tf:
        score_tf[i] = log10((nb_documents / score_tf[i]) + 1)
    return score_tf


def noms_prenoms(dict_identity, list_noms):
    """function giving the list of first and last names associated with each president"""
    dict_presidents = {i: dict_identity[i] for i in list_noms}
    return dict_presidents


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def copy_directory(directory1, directory2):
    list_directory2 = []
    for files in os.listdir(directory1):
        with open(os.path.join(directory1, files), "r", encoding='utf-8') as f1, open(os.path.join(directory2, files),
                                                                                      "w", encoding='utf-8') as f2:
            f2.write(f1.read())
        list_directory2.append(os.path.join(directory2, files))
    return list_directory2


def tf_idf(dic_tf, idf):
    """verifier tf_idf"""
    dic_tf_idf = {i: {j: dic_tf[i][j] * idf[j] for j in dic_tf[i].keys()} for i in dic_tf.keys()}
    return dic_tf_idf


def dict_words(list_path_files):
    list_txt = []
    for path_files in list_path_files:
        with open(path_files, "r", encoding='utf-8') as f1:
            list_txt += f1.read().split(" ")
    set_words = set(list_txt)
    dict_word = dict.fromkeys(set_words, 0)
    return dict_word


def choose_word(dic_words):
    word = input("Choose a word :")
    if word not in dic_words():
        print("Word not present in any of the files.")
    else:
        words = [word]
        return words


def choose_file(dict_pres, pres_names, dict_pres_files, list_files_names):
    answer = "%nul%"
    while answer not in pres_names:
        print("Choose a president in the dictionary below (name) or zero for all :")
        dic_pres = noms_prenoms(dict_pres["p5"], pres_names)
        for j in dic_pres:
            print(j, dic_pres[j], end="  ")
        print()
        answer = input()
        if answer == "0":
            return list_files_names
    key_list = [k for (k, val) in dict_pres_files.items() if val == answer]
    if len(key_list) > 1:
        answer = 0
        while not (0 < answer < len(key_list)):
            print("Be sure to select a specific file :")
            for i, j in enumerate(key_list):
                print(i, j, end="  ")
                print()
            answer = int(input())
        key_list = key_list[answer]
    return key_list


def reponse(type_value, word, files, dict_dict_tf, dict_idf, dict_tf_idf):
    valeur = {}
    if type_value == "tf":
        for file in files:
            for (k, val) in dict_dict_tf[file].items():
                valeur[file].add(k, val)

    elif type_value == "idf":
        for (word_if, val) in dict_idf.items():
            if word_if in word:
                valeur["idf"].add(word_if, val)

    elif type_value == "tf-idf":
        for file in files:
            for (k, val) in dict_tf_idf[file].items():
                valeur[file].add(k, val)
    else:
        print("an error has occurred")

    for i in valeur:
        print(i, end=":\n")
        for word_v, val in valeur[i].items():
            print(str(word_v)+": ", val)
        print()
    print()


def choose_type():
    answer = 0
    types = ["tf", "idf", "tf-idf"]
    while not (1 < answer < 3):
        print("choisi le type de resultat:\n1: for terme-frenquence\n2: for inverse document frenquence\n3: for tf-idf")
        answer = int(input())
    return types[answer]
