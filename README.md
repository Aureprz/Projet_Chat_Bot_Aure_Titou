
# Présentation du Chatbot

Bienvenue, ceci est un projet que nous avons dans notre premier semestre à Efrei Paris et s'apparente à un Chatbot. 
Ce programme ne concerne que la première partie du projet (sur 3). 
Ici, nous nous focalisons sur le traitement de texte. Sans plus attendre, voici ce que le Chatbot peut
faire :

De nombreuses options sont disponibles.

Ce programme se base énormément sur les notions de score TF, IDF et de matrice TF-IDF. Voici la définition de ces termes :

  - **tf** qui représente la fréquence des termes dans un document:
            <div style="text-align:right"><img src="https://cdn.discordapp.com/attachments/1171831701677293568/1180291097793142844/Capture_decran_2023-12-02_003231.png?ex=657ce2be&is=656a6dbe&hm=0f47b247dc90ae3a2b64f0285503c85888cb77b03ab21789f2fafb9a887806f8&" alt="tf" style="opacity: 1;"></div>

  - **idf** qui représente la fréquence inverse d'un terme des documents, c'est-à-dire son importance dans un ensemble de documents:
            <div style="text-align:right"><img src="https://cdn.discordapp.com/attachments/1171831701677293568/1180291098162233354/Capture_decran_2023-12-02_003326.png?ex=657ce2be&is=656a6dbe&hm=35633c2b1608480bec4bbc5b5113ce64243632f960bca9ab90c838d88c3902a5&" alt="idf" style="opacity: 1;"></div>

  - **tf-idf** qui représente l'importance d'un mot à travers un document:
            <div style="text-align:right"><img src="https://cdn.discordapp.com/attachments/1171831701677293568/1180291098418094150/Capture_decran_2023-12-02_003358.png?ex=657ce2be&is=656a6dbe&hm=d180880784bb07ead2440d1a41a3b8dcee118a9a7c50f531eb12e656e2159284&" alt="tf-idf" style="opacity: 1;"></div>

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

* Après le lancement du programme, vous avez le choix parmi 2 options :

- ``1``
  Vous pouvez choisir entre 5 options. Le chatbot vous répondra de manière automatique et basique.
  
    - ``1`` donne la liste des mots considérés comme moins importants dans l'ensemble du corpus (TF-IDF = 0)
  
    - ``2`` affiche les n mots dont le score TF-IDF est le plus élevé, avec n >= 1
  
    - ``3`` montre les mots les plus répétés par le président Chirac, hormi les plus répétés
  
    - ``4`` donne la liste des présidents qui ont prononcé le mot "Nation" au moins une fois
  
    - ``5`` montre la liste des présidents ayant parlé du climat/écologie
        

- ``2``
        Le chatbot vous répondra de manière autonome, toujours dans la thématique du traitement de textes. Par exemple,  les scores TF et IDF ou la matrice TF-IDF d'un document.


        
## Bug: 
Si vous trouvez des bugs n'hésitez pas à les reporter via [issues](https://github.com/Aureprz/Projet_Chat_Bot_Aure_Titou/issues) 
## Todo:

## [Contributeurs](https://github.com/Aureprz/Projet_Chat_Bot_Aure_Titou/settings/access)
- [Aurelien Perez](https://github.com/Aureprz)
- [Titouan Lenain](https://github.com/Artchhh)
