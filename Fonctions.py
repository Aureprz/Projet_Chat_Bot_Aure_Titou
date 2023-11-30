from math import log10
import os


def extraire_nom(list_names_files):
    """function to extract the name of each file (speech)"""
    list_nom = []
    for file_name in list_names_files:
        # Remove "Nomination_" and ".txt"
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
    """function to remove words that appear too often (defined by a predefined list called list_stopword)"""
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
    for word, val in score_tf.items():
        score_tf[word] /= len(list_txt)

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
        score_tf[i] = log10(nb_documents / (score_tf[i]))
    return score_tf


def noms_prenoms(dict_identity, list_noms):
    """function giving the list of first and last names associated with each president"""
    dict_presidents = {i: dict_identity[i] for i in list_noms}
    return dict_presidents


def list_of_files(directory, extension):
    """function that returns each file name entirely in the form of a list"""
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
    """function giving us the TF-IDF matrix for all the words in the files"""
    dic_tf_idf = {i: {j: dic_tf[i][j] * idf[j] for j in dic_tf[i].keys()} for i in dic_tf.keys()}
    return dic_tf_idf


def dict_words(list_path_files):
    """function that returns a dictionary of each word, in a single copy, with a null value"""
    list_txt = []
    for path_files in list_path_files:
        with open(path_files, "r", encoding='utf-8') as f1:
            list_txt += f1.read().split(" ")
    set_words = set(list_txt)
    dict_word = dict.fromkeys(set_words, 0)
    return dict_word


def choose_word(dic_words):
    word = "%null%"
    dic_word = []
    while word != "%end%" or len(dic_word) == 0:
        print("Your selected words:", dic_word)
        word = input("Choose word (or '%all%' for all words) and use '%end%' to exit :\n")
        if word == "%all%":
            dic_word = deref_dic_key(dic_words)
            return dic_word
        if word == "%end%" and len(dic_word) == 0:
            print("Please choose at least a word.")
        elif word not in dic_words.keys():
            print("Word not present in any of the files.")
        else:
            dic_word.append(word)
    return dic_word


def choose_file(dict_pres, pres_names, dict_pres_files, list_files_names):
    answer = "%null%"
    file = []
    while True:
        print("Yours selected files:", file)
        while answer not in pres_names:
            print("Choose a president in the dictionary below (name) or '%all%' for all :")
            dic_pres = noms_prenoms(dict_pres["p5"], pres_names)
            for j in dic_pres:
                print(j, dic_pres[j], end="  ")
            print()
            answer = input()
            if answer == "%all%":
                return list_files_names
            elif answer == "%end%":
                if len(file) != 0:
                    return file
                else:
                    print("Choose at least a file.")
        key_list = [k for (k, val) in dict_pres_files.items() if val == answer]
        if len(key_list) > 1:
            answer = -1
            while not (0 <= answer < len(key_list)):
                print("Be sure to select a specific file :")
                for i, j in enumerate(key_list):
                    print(i, j, end="  ")
                    print()
                answer = int(input())
            key_list = key_list[answer]
            file.append(key_list)
        else:
            file.append(key_list[0])
        answer = "%null%"


def reply(type_value, word, files, dict_dict_tf, dict_idf, dict_tf_idf, interval, type_sort, somme):
    value = {}
    if type_value == "tf":
        for file in files:
            value[file] = {}
            for (k, val) in dict_dict_tf[file].items():
                value[file][k] = val

    elif type_value == "idf":
        value["idf"] = {}
        for (word_if, val) in dict_idf.items():
            if word_if in word:
                value["idf"][word_if] = val

    elif type_value == "tf-idf":
        for file in files:
            value[file] = {}
            for (k, val) in dict_tf_idf[file].items():
                value[file][k] = val
    else:
        print("An error has occurred.")
    f_value = deref_dic_dic(value)
    for name in value:
        for word_v, val in value[name].items():
            if word_v not in word:
                del f_value[name][word_v]
    if somme is True:
        f_value = f_mean(f_value)
    value = deref_dic_dic(f_value)
    for name in value:
        for word_v, val in value[name].items():
            if not (interval[0] <= val <= interval[1]):
                del f_value[name][word_v]
    f_value = func_sorte(f_value, type_sort)
    for name in f_value:
        print()
        print(name, end=":\n")
        for word_v, val in f_value[name].items():
            print(str(word_v)+": ", val, end="  ")
        print()
    print()


def choose_type():
    answer = 0
    types = ["tf", "idf", "tf-idf"]
    while not (1 <= answer <= 3):
        print("Choose the result type :\n1 : For term frequency\n2 : For inverse document frequency\n3 : For TF-IDF")
        answer = int(input())
    return types[answer-1]


def choose_interval():
    a, b = -1, -1
    while not 0 <= a:
        print("Please choose a minimal value (value>=0) :")
        try:
            a = float(input())
        except ValueError:
            print("Incorrect value.")
    while not a <= b:
        print("Please select a maximal value (value>="+str(a)+") :")
        try:
            b = float(input())
        except ValueError:
            print("Incorrect value.")
    interval = [a, b]
    return interval


def deref_dic_dic(dic_dic):
    dic_dic_2 = {}
    for dic in dic_dic:
        dic_dic_2[dic] = {}
        for k, val in dic_dic[dic].items():
            dic_dic_2[dic][k] = val
    return dic_dic_2


def deref_dic_key(dic):
    dic_2 = []
    for k in dic.keys():
        dic_2.append(k)
    return dic_2


def func_sorte(dic, type_sort):
    """Trier les valeurs à l'intérieur de chaque sous-dictionnaire"""
    for key in dic:
        dic[key] = dict(sorted(dic[key].items(), key=lambda item: item[1], reverse=type_sort))
    return dic


def choose_sorte():
    answer = 0
    while not (1 <= answer <= 2):
        print("Choose the result type :\n1 : For ascending order\n2 : For descending order")
        answer = int(input())
    return bool(answer-1)


def f_mean(dic_dic):
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
    dico = {"mean": dico}
    return dico


def choose_mean():
    answer = 0
    while not (1 <= answer <= 2):
        print("Choose if somme is on :\n1 : For off \n2 : For on")
        answer = int(input())
    return bool(answer-1)