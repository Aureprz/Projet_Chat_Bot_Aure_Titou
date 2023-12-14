from tf_idf import *

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
test = input("Entrez une phrase.")
question_global(test, dict_word, dict_idf)
"""
