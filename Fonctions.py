def extraire_nom(list):
    list_nom=[]
    for i in list:
        i = i.split("_")[1]
        j=0
        while 'z'>=i[j] and i[j]>='a' or 'Z'>=i[j] and i[j]>='A' or i[j]==' ':
            j+=1
        list_nom.append(i[:j])
    return(list_nom)


def TF(txt_cleaned):
    list = txt_cleaned.split(" ")
    s = set()
    dict_words = {}
    for i in list:
        s.add(i)
    dict_words = dict.fromkeys(s, 0)
    print(dict_words)
#   for i in list:
#        dict.fromkeys(i, y)
 #       for j in list_fichier_cleaned:
  #          dict_words[i] = y+1
    return dict_words

txt_test ="les fleurs sont bleues mais aussi bleues mais aussi rouges"
print(TF(txt_test))
