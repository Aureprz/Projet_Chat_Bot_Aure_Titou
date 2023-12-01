
# Présentation du Chatbot (Partie 1)

Bienvenue, ceci est un projet que nous avons dans notre premier semestre à Efrei Paris et s'apparente à un Chatbot. 
Ce programme ne concerne que la première partie du projet (sur 3). 
Ici, nous nous focalisons sur le traitement de texte. Sans plus attendre, voici ce que le Chatbot peut
faire :

Parmi un certain nombre de fichiers (fichiers texte), ici les discours de présidents français, vous pouvez en choisir
un et obtenir le nombre d'occurences de chaque mot dans ce fichier à l'aide de la fonction term_frequency.
de tous et obtenir la mesure TF-IDF pour tous les mots du fichier. De même, si vous le souhaitez, vous pouvez obtenir le
TF-IDF de tous les mots du répertoire des fichiers txt.

- Si vous êtes plus intéressé par quelque chose de plus précis, le Chatbot peut vous donner les mots les moins
pertinents (TF-IDF = 0) de tous les fichiers, soit les plus rares, soit ceux que le président choisi utilise
fréquemment.

- De plus, le Chatbot peut vous donner les présidents qui ont, pour point commun, tous utilisé le mot de votre choix
dans leur(s) discours.

Lien GitHub : https://github.com/Aureprz/Projet_Chat_Bot_Aure_Titou

## Guide installation et lancement :

Pour les développeurs, il faut installer [Git](https://git-scm.com/).
Puis, il faut cloner le dépôt :
```bash
git clone https://github.com/Aureprz/Projet_Chat_Bot_Aure_Titou.git
```
Et enfin run le fichier:
```bash
main.py
```

Attention à bien garder à  jour votre code avec `git pull` et  à bien commit les changements avec `git commit`.
Si vous rencontrez des problemes vous pouvez faire un `pip install --upgrade pip`

## Guide d'utilisation :

* aprés le lancement  avez le choix parmi 9 options :

    - ``0``
        Vous donne les paramètres choisis. Si vous n'en avez pas sélectionner, le Chatbot vous renverra la valeur par
        défaut (vous l'avez après l'explication des 6 options)
        * Valeur par défaut du programme :
            - type_value= ``[tf]``
            - file= ``['%all%']``
            - word= ``['%all%']``
            - interval= ``[0, 100]``
            - sort= ``[descending]``
            - mean= ``[ON]``
            - decimal= ``[3]``
            - value= ``[ON]``

    - ``1``
        Vous permet de choisir entre les differents méthodes de calculs du ou des terme(s) sélectionnés
        - ``tf`` qui représente la fréquence des termes dans un document:
                  <div style="text-align:right"><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/dd4f8a91dd0d28a11c00c94a13a315a5b49a8070" alt="tf"></div>
        - ``idf`` qui représente la fréquence inverse des documents:
                  <div style="text-align:right"><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/864fcfdc0c16344c11509f724f1aa7081cf9f657" alt="idf"></div>
        - ``tf-idf`` qui représente l'importance d'un mot:
                  <div style="text-align:right"><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/10109d0e60cc9d50a1ea2f189bac0ac29a030a00" alt="tf-idf"></div>


        

     - ``2``
         Vous permet de sélectionner un ou plusieur discours de président que vous souhaitez étudier. Et vous affiche vos discours déjà selectionner. 
          - ``nom du président`` donnez le nom du président dont vous souhaitez selectionez le discours
          - ``numéro`` si un président a  plus d'un discours, le programme vous lance une sous-option afin de sélectionner le discours spécifiquement
          - ``%all%`` pour selctionner tous les discours
          - ``%end%`` pour terminer la selection
            
    - ``3``
        Vous permet de filtrer le résultat en ne gardant que les mots sélectionnez.  
        - ``mot`` donnez le mot que vous souhaitez selectionner  
        - ``%all%`` pour selctionner tous les mots du corpus  
        - ``%end%`` pour terminer la selection  

    - ``4``
        Vous permet de sélectionner un intervalle dont les bornes sont inclues. Afin de filtrer les scores qui n'appartiennent pas à cet intervalle.
        - ``min`` donnez une valeur minimal: ``min >= 0``
        - ``max`` donnez une valeur maximal : ``max >= min``

    - ``5``
       Vous permet de choisir dans quel ordre seront trier les valeurs afficher à l'écran: soit dans l'ordre croissant ("ascending") soit
        l'ordre décroissant ("descending")
       - ``1`` par ordre croissant
       - ``2`` par ordre décroissant

    - ``6``
        Vous permet de faire la moyenne de toutes les valeurs pour chaque élément choisi suivant le type demandé (tf, idf ou tf-idf) et suivant les fichiers sélectionnés.
        - ``1`` désactivé
        - ``2`` activé

    - ``7``
        Vous permet de choisir le nombre de décimales attendu pour le résultat (s'applique à chaque valeur en fonction de chaque fichier choisi)
        - ``nb`` nombre de décimales au format ex:``1.2e+4`` : ``nb >= 0``
    - ``8``
         Vous permet de choisir si vous souhaitez afficher les valeur ou non
         - ``1`` désactivé
         - ``2`` activé

    - ``9``
        Vous renvoie le résultat de votre sélection 

 
_**Aussi, comme vous avez pu le remarquer ou comme vous le remarquerez, après avoir répondu à votre demande, le Chatbot
vous renverra à nouveau les 9 options à sélectionner. Sachez que tous les paramètres sont sauvegardés.**_

## Todo

## [Contributeurs](https://github.com/Aureprz/Projet_Chat_Bot_Aure_Titou/settings/access)
- [Aureprz](https://github.com/Aureprz)
- [Artchhh](https://github.com/Artchhh)
