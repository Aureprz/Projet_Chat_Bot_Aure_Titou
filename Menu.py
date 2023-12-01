from Fonctions import *


def choose_type():
    answer = 0
    types = ["tf", "idf", "tf-idf"]
    while not (1 <= answer <= 3):
        print("Choose the result type :\n1 : For term frequency\n2 : For inverse document frequency\n3 : For TF-IDF")
        try:
            answer = int(input())
        except ValueError:
            print("Incorrect value.")
    return types[answer-1]


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


def choose_sort():
    answer = 0
    while not (1 <= answer <= 2):
        print("Choose the result type :\n1 : For ascending order\n2 : For descending order")
        try:
            answer = int(input())
        except ValueError:
            print("Incorrect value.")
    return bool(answer-1)


def choose_mean():
    answer = 0
    while not (1 <= answer <= 2):
        print("Choose if somme is on :\n1 : For off \n2 : For on")
        try:
            answer = int(input())
        except ValueError:
            print("Incorrect value.")
    return bool(answer-1)


def choose_decimal():
    answer = -1
    while answer < 0:
        print("select number of decimal")
        try:
            answer = float(input())
        except ValueError:
            print("Incorrect value.")
    return answer


def choose_show_val():
    answer = 0
    while not (1 <= answer <= 2):
        print("Choose if you show value :\n1 : For off \n2 : For on")
        try:
            answer = int(input())
        except ValueError:
            print("Incorrect value.")
    return bool(answer - 1)


def reply(type_value, word, files, dict_dict_tf, dict_idf, dict_tf_idf, interval, type_sort, somme, decimal, show_val):
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
    if somme is True and len(f_value) > 1:
        f_value = f_mean(f_value)
    value = deref_dic_dic(f_value)
    for name in value:
        for word_v, val in value[name].items():
            if not (interval[0] <= val <= interval[1]):
                del f_value[name][word_v]
    f_value = func_sort(f_value, type_sort)
    for name in f_value:
        print()
        print(name, end=":\n")
        for word_v, val in f_value[name].items():
            print(str(word_v), end="")
            if show_val is True:
                print(": {:.{}e}".format(val, decimal), end="")
            print("  ", end="")
        print()
    print()
