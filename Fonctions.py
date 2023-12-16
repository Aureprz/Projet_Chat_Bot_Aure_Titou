
import os


def extraire_nom(list_names_files) -> list:
    """function to extract the name of each file (speech)"""
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
    """function giving the list of first and last names associated with each president"""
    dict_presidents = {i: dict_identity[i] for i in list_noms}
    return dict_presidents


def list_of_files(directory, extension) -> list:
    """function that returns each file name entirely in the form of a list"""
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def copy_directory(directory1, directory2) -> list:
    list_directory2 = []
    for files in os.listdir(directory1):
        with open(os.path.join(directory1, files), "r", encoding='utf-8') as f1, open(os.path.join(directory2, files),
                                                                                      "w", encoding='utf-8') as f2:
            f2.write(f1.read())
        list_directory2.append(os.path.join(directory2, files))
    return list_directory2


def dict_words(list_path_files) -> dict:
    """function that returns a dictionary of each word, in a single copy, with a null value"""
    list_txt = []
    for path_files in list_path_files:
        txt = file_to_str(path_files)
        list_txt += txt.split()
    set_words = set(list_txt)
    dict_word = dict.fromkeys(set_words, 0)
    return dict_word


def deref_dic_dic(dic_dic) -> dict:
    dic_dic_2 = {}
    for dic in dic_dic:
        dic_dic_2[dic] = {}
        for k, val in dic_dic[dic].items():
            dic_dic_2[dic][k] = val
    return dic_dic_2


def deref_dic_key(dic) -> list:  # Lets you use every key (word) with the %all% command
    list_key = []
    for k in dic.keys():
        list_key.append(k)
    return list_key


def func_sort(dic, type_sort) -> dict:
    """Sort values within each sub-dictionary"""
    for key in dic:
        dic[key] = dict(sorted(dic[key].items(), key=lambda item: item[1], reverse=type_sort))
    return dic


def f_mean(dic_dic) -> dict:
    """
    Gives the average of all values according to the word(s) chosen and the type of result selected
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
    dico = {"mean": dico}
    return dico


def file_to_str(file_path):
    with open(file_path, "r", encoding='utf-8') as f1:
        txt = f1.read()
    return txt


def str_to_file(chaine, file_path):
    with open(file_path, "w", encoding='utf-8') as f1:
        f1.write(chaine)


def equivalent_str(name_file, path_directory):
    path_file = os.path.join(path_directory, name_file,)
    text = file_to_str(path_file)
    return text


if __name__ == "__main__":
    print("Do not run this file.")
    print("Run ./main.py")
