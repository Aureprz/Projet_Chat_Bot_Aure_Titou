from tf_idf import *
from Fonctions import *

# list_files_names = list_of_files(directory_base, "txt")


def q1(dict_tf_idf):
    list_words = []
    q = f_mean(dict_tf_idf)
    for (k, val) in q["mean"].items:
        if val == 0:
            list_words.append(k)
    print("Here's the less relevant words (which have a TF-IDF measure equal to 0) :")
    print(list_words)


def q2(dict_2_tf_idf):
    list_words = []
    dict_tf_idf = f_mean(dict_2_tf_idf)
    dict_tf_idf = func_sort(dict_tf_idf, True)
    n = -1
    while n <= 0 or n > 50:
        n = int(input("Choose how many ""important"" word do you want me give you :"))
        while len(list_words) <= n:
            for (k, val) in dict_tf_idf["mean"].items:
                list_words.append(k)
    print("Here's your top", n, "of the most important words across all files")
    return list_words


def q3(dict_tf_idf, tf_dict):
    list_not_relevant = []
    list_words = []
    for i in dict_tf_idf:
        Q = func_sort(tf_dict, True)
    n = -1
    while n <= 0 or n > 50:
        n = int(input("Choose how many ""important"" word do you want me to give you :"))
        while len(list_words) <= n:
            for (k, val) in Q.items():
                if k not in Q:
                    list_words.append(k)
    print("Here's your top", n, "of the most important words in Mr Chirac speech (except less relevant ones) :")
    return list_words
# va sur discord si besoin

def q4():
    list_names = []
    for i in list_files_path: 
        txt = file_to_str(i)
        txt = txt.split()
        if "nation" in txt:
            name_file = os.path.basename(i)
            list_names.append(name_file)
    print("Here's the presidents which said the word ""Nation"" :")
    print(list_names)


def q5():
    list_names = []
    list_climate_terms = ["climat", "écologie", "écologique", "climatique", "changement climatique", "développement durable"]
    for i in list_files_path: 
        txt = file_to_str(i)
        txt = txt.split()
        for j in range (list_climate_terms):
            if list_climate_terms[j] in txt: 
                name_file = os.path.basename(i)
                list_names.append(name_file)
    list_names = set(list_names)
    print("Here's the presidents who spoke about climate in their speeche(s) :")
    print(list_names)

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
    return "non mentioner"


def humanization_answer(txt_q,phrase, name):
    dictionary = {
        "pourquoi": "Car",
        "peux-tu": "Oui, bien sûr!",
        "comment": "De cette manière",
        "où": "A cet endroit",
        "quand": "A ce moment-là",
        "quoi": "cette chose"
    }
    start = txt_q.split()[0].lower()
    if start in dictionary.keys():
        start = dictionary[start]
    elif start == "qui":
        answer = "C'est " + name + "."
        return answer
    else:
        start = "Oui, bien sûr!"
    answer = start + phrase + "."
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
