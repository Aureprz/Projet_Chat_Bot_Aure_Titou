
# Guide du Chatbot (Partie 1)

Bienvenue. Si vous lisez ceci, vous savez probablement déjà de quoi il s'agit. Ceci est un projet que nous avons dans
notre premier semestre à Efrei Paris et s'apparente à un Chatbot. Ce programme ne concerne que la première partie du
projet (sur 3). Ici, nous nous focalisons sur le traitement de texte. Sans plus attendre, voici ce que le Chatbot peut
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

    - ``1``
        Vous permet de choisir entre le score tf, le score idf ou le score tf-idf du ou des terme(s) sélectionnés

     - ``2``
        Sélectionnez le nom du président dont vous souhaitez étudier le discours en donnant son nom. Si un président a
        fait plus d'un discours, le programme vous lance une sous-option afin de sélectionner le discours spécifiquement

    - ``3``
        Donnez autant de mots que vous le souhaitez ou taper "%all%" afin de sélectionner tous les mots possibles

    - ``4``
        Vous lance une série de sous-options telles que la valeur minimale et la valeur maximale de l'intervalle
        souhaitée

    - ``5``
        Ici, vous choisissez dans quel ordre l'affichage va se montrer : soit dans l'ordre croissant ("ascending") soit
        l'ordre décroissant ("descending")

    - ``6``
        Vous permet de faire la moyenne de toutes les valeurs pour chaque élément choisi suivant le type demandé (tf, idf ou tf-idf) et suivant les fichiers sélectionnés

    - ``7``
        Vous permet de choisir le nombre de décimales attendu pour le résultat (s'applique à chaque valeur en fonction de chaque fichier choisi)

    - ``8``
         Vous permet de choisir si vous souhaitez afficher les valeur ou non

    - ``9``
        Vous renvoie le résultat

    - Valeur par défaut du programme :
    - type_value= ``[tf]``
    - file= ``['%all%']``
    - word= ``['%all%']``
    - interval= ``[0, 100]``
    - sort= ``[descending]``
    - mean= ``[ON]``
    - decimal= ``[3]``
    - value= ``[ON]`` 



* Aussi, comme vous avez pu le remarquer ou comme vous le remarquerez, après avoir répondu à votre demande, le Chatbot
  vous renverra à nouveau les 9 options à sélectionner. Sachez que tout est encore en mémoire, c'est-à-dire que si vous
  souhaitez garder les paramètres précédents et seulement changer de mot par exemple, vous n'avez qu'à sélectionner la
  3ème option et donner le mot de votre choix ; le Chatbot vous renverra la solution dans les mêmes conditions que
  précédemment.
## But du programme :

Le principe de ce programme est de créer une sorte de Chatbot. Il traite dans cette 1ère partie le traitement de texte.


## Todo

## [Contributeurs](https://github.com/Aureprz/Projet_Chat_Bot_Aure_Titou/settings/access)
- [Aureprz](https://github.com/Aureprz)
- [Artchhh](https://github.com/Artchhh)
