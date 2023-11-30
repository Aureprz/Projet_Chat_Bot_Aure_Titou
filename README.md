# English
Hi. If you're reading this, you probably already know what this program is about. It's a project we have in our first
semester at Efrei Paris and is kind of a Chatbot. This program's just about the first part of the whole project
(out of 3). Without further ado, here's what the Chatbot can do in this part :

- Out of a certain amount of files (text files), here these are French presidents' speeches, you can choose one of them
and get the term frequency for all the words in the file. Also, if you wish to do so, you can get the TF-IDF measure of
all the words the txt files' directory.

- If you're more interested in something more specific, the Chatbot can either give you the "less relevant" words
(TF-IDF = 0) out of all the files, the rarest ones or the ones the president you chose use frequently.

- Furthermore, the Chatbot can give you the presidents who use which word in their speech(es)

GitHub link : https://github.com/Aureprz/Projet_Chat_Bot_Aure_Titou

## User guide :

To complete your treatment search, you must select all 5 options.
5th option only after you've answered all 4 options. For these 4 options, regardless of the order in which you select
and answer them, there's no problem.
Program default value: file=[%all%], word=[%all%] in the interval [0;100] (i.e. all files and words)
Also, as you may have noticed or will notice, after answering your request, the Chatbot will send you back the 5 options
to select. Please note that everything is still stored in memory, i.e. if you previous settings and just change the word,
for example, all you have to do is select the 3rd option and enter the word of your choice; the Chatbot will return the
solution in the same conditions as before.



# Français
Bienvenue. Si vous lisez ceci, vous savez probablement déjà de quoi il s'agit. C'est un projet que nous avons dans notre
premier semestre à Efrei Paris et s'apparente à un Chatbot. Ce programme ne concerne que la première partie du projet
(sur 3). Ici, nous nous focalisons sur le traitement de texte. Sans plus attendre, voici ce que le Chatbot peut faire :

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

## Guide installation :
## Guide d'utilisation :

## But du programme :

Le principe de ce programme est de créer une sorte de Chatbot. Il traite dans cette 1ère partie le traitement de texte.

### Fichiers :

Ce programme fonctionne autour de 2 fichiers principaux : main.py et Fonctions.py

### Fonctionnement (du main.py) :

* Vous avez le choix parmi 6 options :

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
        Vous renvoie le résultat

    - Valeur par défaut du programme : type=[tf], fichier=[%all%], mot=[%all%], interval [0;100] (soit tous les
                                       fichiers et mots)


* Pour mener à bien votre expérience, vous devez obligatoirement sélectionner les 6 options. Sélectionnez la
  6ème option seulement après avoir répondu aux 5 options. Pour ces 5 options, peut importe l'ordre dans lequel vous les
  sélectionnez et répondez, il n'y a pas de problème.


* Aussi, comme vous avez pu le remarquer ou comme vous le remarquerez, après avoir répondu à votre demande, le Chatbot
  vous renverra à nouveau les 6 options à sélectionner. Sachez que tout est encore en mémoire, c'est-à-dire que si vous
  souhaitez garder les paramètres précédents et seulement changer de mot par exemple, vous n'avez qu'à sélectionner la
  3ème option et donner le mot de votre choix ; le Chatbot vous renverra la solution dans les mêmes conditions que
  précédemment.
## Todo

## [Contributeurs](https://github.com/Aureprz/Projet_Chat_Bot_Aure_Titou/settings/access)
- [Aureprz](https://github.com/Aureprz)
- [Artchhh](https://github.com/Artchhh)
