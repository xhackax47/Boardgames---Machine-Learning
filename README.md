# Board Game Geek

Voici des scrappers pour le site [Board Game Geek] (http://www.boardgamegeek.com).
Chacun d'entre eux sert un objectif distinct dans la collecte de données.

Comme l'attribution des ID n'est pas intuitive (du moins pour moi) pour les jeux, pour obtenir des détails sur le jeu, il faut connaître l'ID à l'avance.
pour obtenir des détails sur le jeu, il faut connaître l'ID au préalable.
En exploitant intelligemment la section des jeux de société de BGG, vous pouvez obtenir les identifiants de tous les jeux de société présents sur le site, ainsi que des informations de base sur ces jeux.
jeux de société du site, ainsi que des informations de base sur leur classement.
Si vous le souhaitez, vous pouvez utiliser les identifiants extraits pour obtenir des informations sur tous les jeux du site.
les différents jeux du site.

Utilisez `scrapy` pour exécuter d'abord `spider.py` avec `scrapy runspider spider.py -o items.csv`.
Ce CSV contiendra les noms des jeux, leurs identifiants et leurs évaluations.
Ensuite, exécutez `python extract_ids.py` pour mettre tous les IDs dans un fichier appelé `ids.txt`.
Ce fichier est ensuite utilisé par le dernier script.
Lancez `python get_game_info.py` pour récupérer tous les jeux dont les IDs sont dans `ids.txt`.
Ces données seront écrites dans un CSV appelé `games.csv` et sont beaucoup plus détaillées
que les informations contenues dans `items.csv`.
Notez qu'il y a plus de 80000 jeux, donc chacune de ces étapes prendra un certain temps.
Pour être gentil avec le site, une requête est faite pour 30 jeux à la fois et est seulement faite
une fois toutes les 2 secondes.
Dans les forums, l'opérateur mentionne que 2 demandes par seconde sont acceptables, mais par sécurité
je n'en fais qu'une toutes les 2 secondes.

Ne pas oublier d'installer les dépendances via "pip install" : 
- Scipy
- Pyplot
- Sklearn