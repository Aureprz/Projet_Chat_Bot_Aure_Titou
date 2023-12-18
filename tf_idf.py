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


def norm_vector(dict_a) -> float:
    norm = 0
    for val in dict_a.values():
        norm += val**2
    norm = sqrt(norm)
    return norm


def cosine_similarity(product_ab, norm_a, norm_b):
    if norm_a != 0 and norm_b != 0:
        cosine = (product_ab / (norm_b * norm_a))
    else:
        cosine = 0.0
    return cosine


def file_pertinence(dict_tf_idf_a, dict_dict_tf_idf):
    dict_simil = {}
    norm_a = norm_vector(dict_tf_idf_a)
    for name, dict_tf_idf_b in dict_dict_tf_idf.items():
        norm_b = norm_vector(dict_tf_idf_b)
        product_scalar_ab = scalar_product(dict_tf_idf_a, dict_tf_idf_b)
        dict_simil[name] = cosine_similarity(product_scalar_ab, norm_b, norm_a)
    sim_max = max(dict_simil, key=dict_simil.get)
    return sim_max


def max_score(dict_tf_idf):
    max_tf_idf = max(dict_tf_idf, key=dict_tf_idf.get)
    return max_tf_idf


if __name__ == "__main__":
    print("Do not run this file.")
    print("Run ./main.py")
