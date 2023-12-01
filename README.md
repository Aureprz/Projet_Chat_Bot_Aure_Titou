
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
-  [main.py](https://github.com/Aureprz/Projet_Chat_Bot_Aure_Titou/blob/master/main.py)

Attention à bien garder à  jour votre code avec `git pull` et  à bien commit les changements avec `git commit`.
Si vous rencontrez des problèmes vous pouvez faire un `pip install --upgrade pip`

## Guide d'utilisation :

* aprés le lancement vous avez le choix parmi 9 options :

    - ``0``
        Vous donne les paramètres choisis. Si vous n'en avez pas sélectionnés, le Chatbot vous renverra la valeur par
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
        Vous permet de choisir entre les différentes méthodes de calcul du ou des terme(s) sélectionnés [(info tf-idf)](https://en.m.wikipedia.org/wiki/Tf%E2%80%93idf)
        - **tf** qui représente la fréquence des termes dans un document:
            <div style="text-align:right"><img src="https://cdn-media-1.freecodecamp.org/images/1*HM0Vcdrx2RApOyjp_ZeW_Q.png" alt="tf" style="opacity: 1;"></div>

        - **idf** qui représente la fréquence inverse des documents:
            <div style="text-align:right"><img src="https://cdn-media-1.freecodecamp.org/images/1*A5YGwFpcTd0YTCdgoiHFUw.png" alt="idf" style="opacity: 1;"></div>

        - **tf-idf** qui représente l'importance d'un mot:
            <div style="text-align:right"><img src="https://cdn-media-1.freecodecamp.org/images/1*nSqHXwOIJ2fa_EFLTh5KYw.png" alt="tf-idf" style="opacity: 1;"></div>


     - ``2``
         Vous permet de sélectionner un ou plusieurs discours de présidents que vous souhaitez étudier. Et vous affiche vos discours déjà sélectionnés. 
          - ``nom du président`` donnez le nom du président dont vous souhaitez sélectionner le discours
          - ``numéro`` si un président a  plus d'un discours, le programme vous lance une sous-option afin de sélectionner le discours spécifiquement
          - ``%all%`` pour sélectionner tous les discours
          - ``%end%`` pour terminer la sélection
            
    - ``3``
        Vous permet de filtrer le résultat en ne gardant que les mots sélectionnés.  
        - ``mot`` donnez le mot que vous souhaitez sélectionner  
        - ``%all%`` pour sélectionner tous les mots du corpus  
        - ``%end%`` pour terminer la sélection  

    - ``4``
        Vous permet de sélectionner un intervalle dont les bornes sont incluses. Afin de filtrer les scores qui n'appartiennent pas à cet intervalle.
        - ``min`` donnez une valeur minimale : ``min >= 0``
        - ``max`` donnez une valeur maximale : ``max >= min``

    - ``5``
       Vous permet de choisir dans quel ordre seront triées les valeurs affichées à l'écran: soit dans l'ordre croissant ("ascending") soit
        l'ordre décroissant ("descending")
       - ``1`` par ordre croissant
       - ``2`` par ordre décroissant

    - ``6``
        Vous permet de faire la moyenne de toutes les valeurs pour chaque élément choisi suivant le type demandé (tf, idf ou tf-idf) et suivant les fichiers sélectionnés.
        - ``1`` désactivé
        - ``2`` activé

    - ``7``
        Vous permet de choisir le nombre de décimales attendues pour le résultat (s'applique à chaque valeur en fonction de chaque fichier choisi)
        - ``nb`` nombre de décimales au format ex:``1.2e+4`` : ``nb >= 0``
    - ``8``
         Vous permet de choisir si vous souhaitez afficher les valeurs ou non
         - ``1`` désactivé
         - ``2`` activé

    - ``9``
        Vous renvoie le résultat de votre sélection 

 
_**Aussi, comme vous avez pu le remarquer ou comme vous le remarquerez, après avoir répondu à votre demande, le Chatbot vous renverra à nouveau les 9 options à sélectionner. Sachez que tous les paramètres sont sauvegardés.**_
## Bug: 
Si vous trouvez des bugs n'hésitez pas à les reporter via [issues](https://github.com/Aureprz/Projet_Chat_Bot_Aure_Titou/issues) 
## Todo:

## [Contributeurs](https://github.com/Aureprz/Projet_Chat_Bot_Aure_Titou/settings/access)
- [Aureprz](https://github.com/Aureprz)
- [Artchhh](https://github.com/Artchhh)
