import pandas

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 12:13:23 2023

@author: samy_
"""

# Importer la bibliothèque pandas.
import pandas
# Lire les données.
games = pandas.read_csv("games.csv")
# Afficher les noms de colonnes du DataFrame games.
print("Colonne : " + games.columns)
# Afficher les dimensions du Dataframe ex: 81312 lignes et 20 colonnes)
print("Dimensions : " + str(games.shape))
