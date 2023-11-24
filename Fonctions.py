from math import log10
import os


def extraire_nom(list_names_files):
    """function to extract the name of each file (speech)"""
    list_nom = set()
    for file_name in list_names_files:
        # Remove "Nomination_" et ".txt"
        name = file_name.split("_")[1].split(".txt")[0]
        j = len(name)-1
        while not (name[j].isalpha() or name[j].isspace()):
            j -= 1
        list_nom.add(name[:j+1])
    return list(list_nom)


def punctuation(file_path, list_punctuation):
    """ function removing each punctuation element, such as commas or hyphens, from files"""
    with open(file_path, "r") as f1:
        txt = f1.read()
        translation_table = str.maketrans(list_punctuation, " " * len(list_punctuation))
        txt = txt.translate(translation_table)
        txt = " ".join(txt.split())

    with open(file_path, "w") as f1:
        f1.write(txt)


def stopword(file_path, list_stopword):
    """function to remove words that appear too often (defined by a predefined list)"""
    text_c = []
    with open(file_path, "r") as f1:
        text = f1.readline().split()
        text_c = " ".join(word for word in text if word not in list_stopword)
    with open(file_path, "w") as f1:
        f1.write(text_c)


def minuscule(file_path):
    """function transforming the text of each file into lowercase letters"""
    with open(file_path, "r") as f1:
        txt = f1.read()
    translation_table = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")
    txt = txt.translate(translation_table)
    with open(file_path, "w") as f1:
        f1.write(txt)


def term_frequency(name_files_cleaned, dict_word):
    """TF function calculating the frequency of occurrence of a term in such file"""
    with open(name_files_cleaned, "r") as f1:
        list_txt = f1.read().split(" ")
    for i in list_txt:
        dict_word[i] = dict_word[i]+1
    return dict_word


def inverse_document_frequency(list_dict_term, dict_word):
    """IDF function calculating the importance of a term across all existing files"""
    for dict_term in list_dict_term:
        for word in dict_term.keys():
            dict_word[word] = dict_word[word] + 1

    nb_documents = len(list_dict_term)
    for i in dict_word:
        dict_word[i] = log10((nb_documents / dict_word[i]) + 1)

    return dict_word


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
    for files in os.listdir(directory1):
        with open(files, "r") as f1, open(os.path.join(directory2, files), "w") as f2:
            f2.write(f1.read())


def tf_idf(dic_tf, idf):
    """verifier tf_idf"""
    dic_tf_idf = {i: {j: dic_tf[i][j] * idf[j] for j in dic_tf[i].keys()} for i in dic_tf.keys()}
    return dic_tf_idf


def dict_words(list_path_files):
    list_txt = []
    for path_files in list_path_files:
        with open(path_files, "r") as f1:
            list_txt += f1.read().split(" ")
    set_words = set(list_txt)
    dict_word = dict.fromkeys(set_words, 0)
    return dict_word
