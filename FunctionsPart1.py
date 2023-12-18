from tf_idf import *
from Fonctions import *
from main import *
# list_files_names = list_of_files(directory_base, "txt")


def q1(dict_tf_idf):
    list_words = []
    dict_tf_idf = f_mean(dict_tf_idf)
    for (k, val) in dict_tf_idf["mean"].items:
        if val == 0:
            list_words.append(k)
    print("Voici les mots considérés comme moins importants (soit leure score TF-IDF = 0) :")
    print(list_words)


def q2(dict_2_tf_idf):
    list_words = []
    dict_tf_idf = f_mean(dict_2_tf_idf)
    dict_tf_idf = func_sort(dict_tf_idf, True)
    n = -1
    while n <= 0 or n > 50:
        n = int(input("choisissez combien de mots ""important"" vous souhaitez que je vous donne :"))
        while len(list_words) <= n:
            for (k, val) in dict_tf_idf["mean"].items:
                list_words.append(k)
    print("voici votre top", n, "des mots les plus importants à travers tous les fichiers")
    return list_words


def q3(dict_tf_idf, tf_dict):
    list_words_not_relevant = []
    list_words = []
    for i in dict_tf_idf:
        Q = func_sort(tf_dict, True)
    n = -1
    while n <= 0 or n > 50:
        n = int(input("Choisissez combien de mots  :"))
        while len(list_words) <= n:
            for (k, val) in Q.items():
                if k not in Q:
                    list_words.append(k)
    print("voici votre top", n, "des mots les plus répétés par le président Chirac (excepté ceux qui considérés comme"
                                "moins importants) :")
    return list_words


def q4():
    list_names = []
    for i in list_files_path: 
        txt = file_to_str(i)
        txt = txt.split()
        if "nation" in txt:
            name_file = os.path.basename(i)
            list_names.append(name_file)
    print("Voici tous les présidents qui ont prononcé au moins une fois le mot ""nation"" :")
    print(list_names)


def q5():
    list_names = []
    list_climate_terms = ["climat", "écologie", "écologique", "climatique", "changement climatique", "développement durable"]
    for i in list_files_path: 
        txt = file_to_str(i)
        txt = txt.split()
        for j in range (len(list_climate_terms)-1):
            if list_climate_terms[j] in txt: 
                name_file = os.path.basename(i)
                list_names.append(name_file)
    list_names = set(list_names)
    print("Les présidents qui ont parlé d'écologie/climat dans leur(s) discours sont :")
    print(list_names)

def f_tf_idf_q(txt, dict_word, dict_idf):
    txt_question = clean(txt)
    tf_question = term_frequency(dict_word, txt=txt_question)
    tf_idf_question = tf_idf(dict_idf, dict_tf=tf_question)["Score"]
    return tf_idf_question


def answer_sentence(text1, words):
    list_sentence = text1.split(".")
    for sentence in list_sentence:
        if words in sentence:
            return sentence
    return "Non mentioné"


def humanization_answer(txt_q,sentence, name):
    dictionary = {
        "pourquoi": "Car",
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
    answer = start + phrase + "."
    return answer


def question_global(txt_quest, dict_word1, dict_idf_1, dict_dict_tf_idf1, directory_base_):
    tf_idf_q = f_tf_idf_q(txt_quest, dict_word1, dict_idf_1)
    sim_max_name = file_pertinence(tf_idf_q, dict_dict_tf_idf1)
    name = [sim_max_name]
    name_president = extraire_nom(name)[0]
    text_speach = equivalent_str(sim_max_name, directory_base_)
    words = max_score(tf_idf_q)
    phrase = answer_sentence(text_speach, words)
    answer = humanization_answer(txt_quest, phrase, name_president)
    return answer
