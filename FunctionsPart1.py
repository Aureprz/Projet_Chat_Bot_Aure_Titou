from tf_idf import *
from Fonctions import *
from main import *

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


def q3(tf_dict):
    with open("stop_words_french.txt", "r") as f: # ceux ne sont pas les mots non-importants (pas utile)
        list_words = []
    Q = func_sort(tf_dict, True)
    n = -1
    while n <= 0 or n > 50:
        n = int(input("Choose how many ""important"" word do you want me give you :"))
        while len(list_words) <= n:
            for (k, val) in Q.items():
                if k not in f:
                    list_words.append(k)
    print("Here's your top", n, "of the most important words in Mr Chirac speech (except less relevant ones) :")
    return list_words
# va sur discord si besoin

def q4():
    list_names = []
    for i in "./cleaned": # utilise plutôt list_files_path (la variable)
        with open(i, "r") as f: # utilise plutôt file_to_str ( la fonction) et .split()
            if "nation" in f:  # c bien
                list_names.append(i) # nom_fichier = os.path.basename(chemin_acces)
                # bonne chance (;

    print("Here's the presidents which said the word ""Nation"" ")


def q5():
    L=[]


def q6():
    L=[]


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

def humanization_answer(txt_q,phrase):
    dictionary = {
        "pourquoi": "Car",
        "peux-tu": "Oui, bien sûr!",
        "comment": "De cette manière",
        "où": "A cet endroit",
        "quand": "A ce moment-là",
        "qui": "cette personne",
        "quoi": "cette chose"
    }
    start = txt_q.split()[0].lower()
    if start in dictionary.keys():
        start = dictionary[start]
    else:
        start = "Oui, bien sûr!"
    answer = start + phrase + "."
    return answer
def question_global(txt_q, dict_word, dict_idf_1, dict_dict_tf_idf, directory_base_):
    tf_idf_q = f_tf_idf_q(txt_q, dict_word, dict_idf_1)
    sim_max_name = file_pertinence(tf_idf_q, dict_dict_tf_idf)
    text_speach = equivalent_str(sim_max_name, directory_base_)
    words = max_score(tf_idf_q)
    phrase = phrase_answer(text_speach, words)
    answer = humanization_answer(txt_q,phrase)
    return answer
