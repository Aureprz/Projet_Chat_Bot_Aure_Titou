from tf_idf import *
from Fonctions import *
from main import *

list_files_names = list_of_files(directory_base, "txt")
def Q1(TF_IDF):
    L = []
    Q = f_mean(TF_IDF)
    for (k, val) in Q["mean"].items:
        if val == 0 :
            L.append(k)
    print("Here's the less relevant words (which have a TF-IDF measure equal to 0) :")
    print(L)

def Q2(TF_IDF):
    L = []
    Q = f_mean(TF_IDF)
    Q = func_sort(Q, True)
    n = -1
    while n <= 0 and n > 50:
        n = int(input("Choose how many ""important"" word do you want me give you :"))
        while len(L) <= n :
            for (k, val) in Q["mean"].items:
                L.append(k)
    print("Here's your top", n, "of the most important words across all files")
    return L

def Q3(tf_dict):
    with open("stop_words_french.txt", "r") as f:
    L = []
    Q = func_sort(tf_dict, True)
    n = -1
    while n <= 0 and n > 50:
        n = int(input("Choose how many ""important"" word do you want me give you :"))
        while len(L) <= n:
            for (k, val) in Q.items:
                if k not in f:
                    L.append(k)
    print("Here's your top", n, "of the most important words in Mr Chirac speech (except less relevant ones) :")
    return L

def Q4():
    L=[]
    for i in "./cleaned" :
        with open(i, "r") as f:
            if "nation" in f:
                L.append(i)

    print("Here's the presidents which said the word ""Nation"" ")

def Q5():
    L=[]

def Q6():
    L=[]

def question_global(txt, dict_word, dict_idf):
    txt_question = clean(txt)
    tf_question = term_frequency(dict_word, txt=txt_question)
    tf_idf_question = tf_idf(dict_idf, dict_tf=tf_question)
    print(tf_idf_question)


"""
list_punctuation1 = [
                    '.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '<', '>', "'", '"', '/',
                    '|', '@', '#', '$', '%', '^', '&', '*', '_', '+', '-', '=', '~', '`', "\n", "\""
                    ]
test = input("Give me a sentence :")
question_global(test, dict_word, dict_idf)
"""
