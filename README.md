# Guide du Chatbot (Partie 1)

Bienvenue. Si vous lisez ceci, vous savez probablement déjà de quoi il s'agit. Ceci un projet que nous avons dans notre
premier semestre à Efrei Paris et s'apparente à un Chatbot. Ce programme ne concerne que la première partie du projet
(sur 3). Ici, nous nous focalisons sur le traitement de texte. Sans plus attendre, voyons comment l'utiliser :


Lien GitHub : https://github.com/Aureprz/Projet_Chat_Bot_Aure_Titou

## Guide d'installation et de lancement :

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


## But du programme :

Le principe de ce programme est de créer une sorte de Chatbot. Il traite dans cette 1ère partie le traitement de texte.


## Guide d'utilisation :

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

    - Valeur par défaut du programme :
      ``type=[tf], fichier=[%all%], mot=[%all%], interval [0;100]`` (soit tous les fichiers et mots)
 
    -  Sous-option ``%all`` :
      Si vous ne souhaitez pas choisir d'éléments en particulier, la commande ``%all%`` afin de sélectionner l'entièreté des éléments définis par l'option choisie.
      Par exemple, si vous avez la choisi l'option ``2``, utiliser cette commande vous permet de prendre l'ensemble des fichiers/discours comme réponse.

     - Sous-option ``%end%`` :
       La commande ``%end%`` vous permet de revenir d'un cran en arrière. Si vous utilisez cette commande sans avoir sélectionner une option (celles du menu principal,
       soit celles numérotés de ``1`` à ``6``), le programme vous renverra une erreur.


* Aussi, comme vous avez pu le remarquer ou comme vous le remarquerez, après avoir répondu à votre demande, le Chatbot
  vous renverra à nouveau les 6 options à sélectionner. Sachez que tout est encore en mémoire, c'est-à-dire que si vous
  souhaitez garder les paramètres précédents et seulement changer de mot par exemple, vous n'avez qu'à sélectionner la
  3ème option et donner le mot de votre choix ; le Chatbot vous renverra la solution dans les mêmes conditions que
  précédemment.
  
## Todo

## [Contributeurs](https://github.com/Aureprz/Projet_Chat_Bot_Aure_Titou/settings/access)
- [Aureprz](https://github.com/Aureprz)
- [Artchhh](https://github.com/Artchhh)
