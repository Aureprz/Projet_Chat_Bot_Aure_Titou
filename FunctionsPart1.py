from tf_idf import *
from Fonctions import *


def q1(dict_tf_idf):
    list_words = []
    dict_tf_idf = f_mean(dict_tf_idf)
    for (k, val) in dict_tf_idf.items():
        if val == 0:
            list_words.append(k)
    print("Voici les mots considérés comme moins importants (soit leure score TF-IDF = 0) :")
    for word in list_words:
        print(word, end="; ")
    print("\n")


def q2(dict_2_tf_idf):
    list_words = []
    dict_tf_idf = f_mean(dict_2_tf_idf)
    dict_tf_idf = func_sort(dict_tf_idf, True)
    n = -1
    while n <= 0 or n > len(dict_tf_idf):
        n = int(input("Choose how many 'important' word do you want me to give you (nb<=" + str(len(dict_tf_idf)) + ") :"
                      ))
        list_k = list(dict_tf_idf.keys())
        for i in range(n):
            list_words.append(list_k[i])
    print("voici votre top", n, "des mots les plus importants à travers tous les fichiers")
    for word in list_words:
        print(word, end="; ")
    print("\n")


def q3(dict_dict_tf, dict_dict_idf):
    nb_mot_demander = 0
    list_files = ["Nomination_Chirac1.txt", "Nomination_Chirac2.txt"]
    dict_words_chirac = {}
    for name_file in list_files:
        file_path = os.path.join("cleaned", name_file)
        nb = count_word(file_path)
        for k, val in dict_dict_tf[name_file].items():
            if dict_dict_idf[k] != 0:
                dict_words_chirac[k] = dict_words_chirac.get(k, 0) + (val * nb)
    list_words_chirac = list(func_sort(dict_words_chirac, True).keys())
    n = -1
    while n <= 0 or n > len(list_words_chirac):
        n = int(input("Choose how many 'important' word do you want me to give you (nb<=" + str(len(list_words_chirac))
                      + ") :"))
    list_words_chirac = list_words_chirac[:n]
    print("Voici votre top", n, "des mots les plus importants du discours de M.Chirac (sauf ceux qui sont moins "
                                "pertinents):")
    for word in list_words_chirac:
        print(word, end="; ")
    print("\n")


def q4(dict_dict_tf):
    dict_names = {}
    for name_dict in dict_dict_tf:
        file_path = os.path.join("cleaned", name_dict)
        nb = count_word(file_path)
        name_president = "".join(extraire_nom([name_dict]))
        dict_names[name_president] = dict_dict_tf[name_dict]["nation"] * nb
    list_names = list(func_sort(dict_names, True).keys())
    print("""Voici les présidents qui ont le plus parlé de la "nation", triés dans l'ordre décroissant:""")
    for name in list_names:
        print(name, end="  ")
    print("\n")


def q5(dict_pres_files):
    list_names = set()
    for name_files, name in dict_pres_files.items():
        file_path = os.path.join("cleaned", name_files)
        txt_file = file_to_str(file_path)
        txt_file = txt_file.split()
        if ("nation" or "climat") in txt_file:
            list_names.add(name)
    print("""Voici les présidents qui ont dit le mot "climat" ou "écologie":""")
    for name in list_names:
        print(name, end="  ")
    print("\n")



def f_tf_idf_q(txt, dict_word, dict_idf):
    txt_question = clean(txt)
    tf_question = term_frequency(dict_word, txt=txt_question)
    tf_idf_question = tf_idf(dict_idf, dict_tf=tf_question)["Score"]
    return tf_idf_question


def phrase_answer(text1, words):
    list_sentence = text1.split(".")
    for sentence in list_sentence:
        if words in sentence:
            return sentence
    return "Non mentioné"


def humanization_answer(txt_q, sentence, name):
    dictionary = {
        "pourquoi": "Car,",
        "peux-tu": "Oui, bien sûr !",
        "comment": "De cette manière,",
        "où": "A cet endroit,",
        "quand": "A ce moment-là,",
        "quoi": "cette chose"
    }
    start = txt_q.split()[0].lower()
    if start in dictionary.keys():
        start = dictionary[start]
    elif start == "qui":
        answer = "C'est " + name + "."
        return answer
    else:
        start = "Oui, bien sûr !"
    answer = start + sentence + "."
    return answer


def question_global(txt_quest, dict_word1, dict_idf_1, dict_dict_tf_idf1, directory_base_):
    tf_idf_q = f_tf_idf_q(txt_quest, dict_word1, dict_idf_1)
    sim_max_name = file_pertinence(tf_idf_q, dict_dict_tf_idf1)
    name = [sim_max_name]
    name_president = extraire_nom(name)[0]
    text_speach = equivalent_str(sim_max_name, directory_base_)
    words = max_score(tf_idf_q)
    phrase = phrase_answer(text_speach, words)
    answer = humanization_answer(txt_quest, phrase, name_president)
    return answer
