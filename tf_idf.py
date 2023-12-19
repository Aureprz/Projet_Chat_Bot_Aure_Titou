from math import log10, sqrt
from Fonctions import *
"""
Regroupe les différentes fonctions en lien avec le traitement de texte
"""


def minuscule(txt) -> str:
    """
    Fonction transformant le texte de chaque fichier en lettres minuscules
    :param txt: texte d'un fichier
    :return: texte
    """
    txt = txt.lower()
    return txt


def punctuation(txt) -> str:
    """
    fonction supprimant chaque élément de ponctuation, comme les virgules ou les traits d’union, des fichiers
    :param txt: texte d'un fichier
    :return: texte
    """
    list_punctuation = [
        '.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '<', '>', "'", '"', '/',
        '|', '@', '#', '$', '%', '^', '&', '*', '_', '+', '-', '=', '~', '`', "\n", "\""
    ]
    list_punctuation = "".join(list_punctuation)
    translation_table = str.maketrans(list_punctuation, " " * len(list_punctuation))
    txt = txt.translate(translation_table)
    txt = " ".join(txt.split())
    return txt


def clean(text) -> str:
    """
    Regroupe les différentes étapes du traitement de texte
    :param text: texte d'un fichier
    :return: texte
    """
    text = text.lower()
    text = punctuation(text)
    return text


def term_frequency(dict_word, path_file_txt=None, txt="") -> dict:
    """
    Fonction TF calculant la fréquence d’apparition d’un terme dans ce fichier
    :param dict_word: dictionnaire des mots présent dans le corpus
    :param path_file_txt: chemin du fichier
    :param txt: text d'un fichier
    :return: un dictionnaire qui  associe à chaque mot du fichier un score de terme fréquence
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
    """
    Fonction IDF calculant l’importance d’un terme dans tous les fichiers existants
    :param dict_word: dictionnaire des mots présent dans le corpus
    :param dict_dict_tf: dictionnaire des dictionnaires TF
    :param dict_tf: dictionnaire TF
    :return: dictionnaire qui associe un score inverse document fréquence à chaque mot du corpus
    """
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
    """
    fonction nous donnant la matrice TF-IDF pour tous les mots dans les fichiers du corpus
    :param idf: dictionnaire IDF
    :param dict_dict_tf: dictionnaire de dictionnaire TF
    :param dict_tf: dictionnaire TF
    :return: Matrice TF-IDF (dictionnaire de dictionnaire)
    """
    if dict_tf is not None:
        dict_dict_tf = {"Score": dict_tf}
    if dict_dict_tf is not None:
        dic_tf_idf = {i: {j: dict_dict_tf[i][j] * idf[j] for j in dict_dict_tf[i].keys()} for i in dict_dict_tf.keys()}
        return dic_tf_idf


def scalar_product(dict_a, dict_b):
    """
    Cette fonction calcule le produit scalaire de 2 document
    :param dict_a: dictionnaire de valeurs a
    :param dict_b:dictionnaire de valeurs b
    :return: produit scalaire de a et b
    """
    product_ab = 0
    for key in dict_a.keys():
        product_ab += dict_a[key] * dict_b[key]
    return product_ab


def norm_vector(dict_a) -> float:
    """
    Cette fonction calcule la norm d'un dictionnaire
    :param dict_a: dictionnaire dont on cherche la norme
    :return: la norm du dictionnaire a
    """
    norm = 0
    for val in dict_a.values():
        norm += val**2
    norm = sqrt(norm)
    return norm


def cosine_similarity(product_ab, norm_a, norm_b):
    """
    Cette fonction calcule le cosinus similarité de 2 vecteurs (dictionnaires)
    :param product_ab: produit scalaire de a et b
    :param norm_a: norme du dictionnaire a
    :param norm_b: norme du dictionnaire b
    :return: le cosinus de similarité
    """
    if norm_a != 0 and norm_b != 0:
        cosine = (product_ab / (norm_b * norm_a))
    else:
        cosine = 0.0
    return cosine


def file_pertinence(dict_tf_idf_a, dict_dict_tf_idf):
    """
    Cette fonction cherche la pertinence d'un fichier par rapport a la question grâce au cosinus de similarité
    :param dict_tf_idf_a: dictionnaire TF-IDF de la question
    :param dict_dict_tf_idf: ensemble des dictionnaires TF-IDF du corpus
    :return: Le nom du fichier avec la plus grande similarité
    """
    dict_simil = {}
    norm_a = norm_vector(dict_tf_idf_a)
    for name, dict_tf_idf_b in dict_dict_tf_idf.items():
        norm_b = norm_vector(dict_tf_idf_b)
        product_scalar_ab = scalar_product(dict_tf_idf_a, dict_tf_idf_b)
        dict_simil[name] = cosine_similarity(product_scalar_ab, norm_b, norm_a)
    sim_max = max(dict_simil, key=dict_simil.get)
    return sim_max


def max_score(dict_tf_idf):
    """
    Cette fonction permettant de trouver le mot avec le score TF-IDF le plus élever dans la question
    :param dict_tf_idf: dictionnaire TF-IDF de la question
    :return: valeur maximum de la question
    """
    max_tf_idf = max(dict_tf_idf, key=dict_tf_idf.get)
    return max_tf_idf


if __name__ == "__main__":
    print("Do not run this file.")
    print("Run ./main.py")
