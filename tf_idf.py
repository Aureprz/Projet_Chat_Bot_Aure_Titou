from math import log10, sqrt
from Fonctions import *


def minuscule(txt) -> str:
    """function transforming the text of each file into lowercase letters"""
    txt = txt.lower()
    return txt


def punctuation(txt) -> str:
    """ function removing each punctuation element, such as commas or hyphens, from files"""
    list_punctuation = [
        '.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '<', '>', "'", '"', '/',
        '|', '@', '#', '$', '%', '^', '&', '*', '_', '+', '-', '=', '~', '`', "\n", "\""
    ]
    list_punctuation = "".join(list_punctuation)
    translation_table = str.maketrans(list_punctuation, " " * len(list_punctuation))
    txt = txt.translate(translation_table)
    txt = " ".join(txt.split())
    return txt


def stopword(text, list_stopword) -> str:
    """function to remove words that appear too often (defined by a predefined list called list_stopword)"""
    text_c = " ".join(word for word in text if word not in list_stopword)
    return text_c


def clean(text) -> str:
    text = text.lower()
    text = punctuation(text)
    return text


def term_frequency(dict_word, path_file_txt=None, txt="") -> dict:
    """
    TF function calculating the frequency of occurrence of a term in such file
    """
    score_tf = dict_word.copy()
    if path_file_txt is not None:
        txt = file_to_str(path_file_txt)
    if txt is not None:
        list_txt = txt.split()
        for i in list_txt:
            if i in score_tf:
                score_tf[i] = score_tf[i]+1
        for word, val in score_tf.items():
            score_tf[word] /= len(list_txt)

    return score_tf


def inverse_document_frequency(dict_word, dict_dict_tf=None, dict_tf=None) -> dict:
    """IDF function calculating the importance of a term across all existing files"""
    score_idf = dict_word.copy()
    if dict_tf is not None:
        dict_dict_tf = {"Score": dict_tf}
    if dict_dict_tf is not None:
        for dict_TF in dict_dict_tf.values():
            for word in dict_TF.keys():
                if dict_TF[word] > 0:
                    score_idf[word] = score_idf[word] + 1

        nb_documents = len(dict_dict_tf)
        for i in score_idf:
            score_idf[i] = log10(nb_documents / (score_idf[i]))
    return score_idf


def tf_idf(idf, dict_dict_tf=None, dict_tf=None) -> dict:
    """function giving us the TF-IDF matrix for all the words in the files"""
    if dict_tf is not None:
        dict_dict_tf = {"Score": dict_tf}
    if dict_dict_tf is not None:
        dic_tf_idf = {i: {j: dict_dict_tf[i][j] * idf[j] for j in dict_dict_tf[i].keys()} for i in dict_dict_tf.keys()}
        return dic_tf_idf


def scalar_product(dict_a, dict_b):
    product_ab = 0
    for key in dict_a.keys():
        product_ab += dict_a[key] * dict_b[key]
    return product_ab


def norm_vector(dict_a):
    norm = 0
    for val in dict_a:
        norm += val**2
    norm = sqrt(norm)
    return norm


def cosine_similarity(product_ab, norm_a, norm_b):
    cosine = (product_ab / (norm_b * norm_a))
    return cosine

if __name__ == "__main__":
    print("Do not run this file.")
    print("Run ./main.py")



