import pandas as pd
import matplotlib.pyplot as plt

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 12:13:23 2023

@author: samy_
"""

# Lire les données.
games = pd.read_csv("datasets/games.csv")

# Afficher les noms de colonnes du DataFrame games.
print("Colonne : " + games.columns)
# Afficher les dimensions du Dataframe ex: 81312 lignes et 20 colonnes)
print("Dimensions : " + str(games.shape))
# Histogramme de toutes les notes de la colonne average_rating.
plt.hist(games["average_rating"])
# Afficher le graphique
plt.show()
