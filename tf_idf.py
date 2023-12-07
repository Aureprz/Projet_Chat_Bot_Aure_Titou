from math import log10
from Fonctions import *


def minuscule(txt) -> str:
    """function transforming the text of each file into lowercase letters"""
    txt = txt.lower()
    return txt


def punctuation(txt, list_punctuation) -> str:
    """ function removing each punctuation element, such as commas or hyphens, from files"""
    list_punctuation = "".join(list_punctuation)
    translation_table = str.maketrans(list_punctuation, " " * len(list_punctuation))
    txt = txt.translate(translation_table)
    txt = " ".join(txt.split())
    return txt


def stopword(text, list_stopword) -> str:
    """function to remove words that appear too often (defined by a predefined list called list_stopword)"""
    text_c = " ".join(word for word in text if word not in list_stopword)
    return text_c


def term_frequency(name_file_cleaned, dict_word) -> dict:
    """TF function calculating the frequency of occurrence of a term in such file"""
    score_tf = dict_word.copy()
    list_txt = file_to_str(name_file_cleaned).split(" ")
    for i in list_txt:
        score_tf[i] = score_tf[i]+1
    for word, val in score_tf.items():
        score_tf[word] /= len(list_txt)

    return score_tf


def inverse_document_frequency(list_dict_term, dict_word) -> dict:
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


def tf_idf(dic_tf, idf) -> dict:
    """function giving us the TF-IDF matrix for all the words in the files"""
    dic_tf_idf = {i: {j: dic_tf[i][j] * idf[j] for j in dic_tf[i].keys()} for i in dic_tf.keys()}
    return dic_tf_idf


if __name__ == "__main__":
    print("Do not run this file.")
    print("Run ./main.py")
