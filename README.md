# Boardgames - Machine Learning

Ce projet me sert à expérimenter le machine learning à travers du Dataset de boardgamegeek.com.

 ![Example de fonctionnement de l'IA 1](https://i.ibb.co/P9PL7v0/Capture-d-cran-2023-02-04-164420.png)
 ![Example de fonctionnement de l'IA 2](https://i.ibb.co/xgbzmJc/Capture-d-cran-2023-02-04-164500.png)

## Environnement

Nous aurons besoin de Python dernière version, l'IDE Spyder et Anaconda3 pour mettre tout en place.

- [Python](https://www.python.org/downloads/)
- [Spyder IDE](https://www.spyder-ide.org/)
- [Anaconda3](https://www.anaconda.com/)

## Dépendances

Afin d'installer les dépendances nécessaires, il vaut mieux utiliser Anaconda pour créer un environnement virtuel : 

- Vous devez créer un nouvel environnement Conda avec les modules que vous voulez utiliser avec Spyder et y inclure spyder-kernels. Par exemple, si vous souhaitez utiliser scikit-learn, ouvrez votre terminal ou l'invite Anaconda sous Windows et exécutez les commandes suivantes pour créer l'environnement, l'activer et installer les modules/dépendances nécessaires:

```
conda create -n spyder-env -y
conda activate spyder-env
conda install spyder-kernels scikit-learn -y
conda install nomdumoduleainstaller
```

- Enfin, vous devez connecter Spyder à cet environnement en modifiant l'interpréteur Python par défaut de Spyder. Pour ce faire, cliquez sur le nom de l'environnement actuel dans la barre d'état, puis cliquez sur Changer l'environnement par défaut dans les Préférences.

- La boîte de dialogue Préférences s'ouvre alors dans la section Interpréteur Python. Ici, sélectionnez l'option Utiliser l'interpréteur Python suivant, et utilisez la liste déroulante ci-dessous pour sélectionner votre environnement préféré. S'il n'est pas répertorié, utilisez la zone de texte ou le bouton Select file pour saisir le chemin d'accès à l'interpréteur Python que vous souhaitez utiliser.

- Votre nouvel environnement ne sera listé ici que si vous avez installé Miniconda (ou Anaconda) dans le chemin par défaut comme indiqué dans le tableau ci-dessus.

- Cliquez sur Restart kernel dans le menu Consoles pour que ce changement prenne effet.

En cas de besoin : 
- Utilisez `scrapy` pour exécuter d'abord `spider.py` avec `scrapy runspider spider.py -o items.csv`. Ce CSV contiendra les noms des jeux, leurs identifiants et leurs évaluations. 
- Ensuite, exécutez `python extract_ids.py` pour mettre tous les IDs dans un fichier appelé `ids.txt`. Ce fichier est ensuite utilisé par le dernier script. 
- Lancez `python get_game_info.py` pour récupérer tous les jeux dont les IDs sont dans `ids.txt`. Ces données seront écrites dans un CSV appelé `games.csv` et sont beaucoup plus détaillées que les informations contenues dans `items.csv`. 
*Notez qu'il y a plus de 80000 jeux, donc chacune de ces étapes prendra un certain temps. Pour être gentil avec le site, une requête est faite pour 30 jeux à la fois et est seulement faite une fois toutes les 2 secondes. Dans les forums, l'opérateur mentionne que 2 demandes par seconde sont acceptables, mais par sécurité je n'en fais qu'une toutes les 2 secondes.*