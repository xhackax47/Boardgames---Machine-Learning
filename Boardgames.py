import pandas as pd
import matplotlib.pyplot as plt
import time
#from sklearn.cluster import KMeans


# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 12:13:23 2023

@author: samy_
"""

# Variables

start = "INITIALISATION ET DEMARRAGE DU PROGRAMME PRINCIPAL"
end = "FIN DU PROGRAMME"
graphStart = "Génération du graphique..."
arating = "average_rating"
urated = "users_rated"
delaiStart = 5
delaiGraph = 2.5
# Lire les données.
games = pd.read_csv("datasets/games.csv")

# Fonctions

def graphParColonne(colonne):
    """Génération d'un graphique à partir d'une colonne."""
    # Histogramme de toutes les notes de la colonne average_rating.
    plt.hist(games[colonne])
    # Afficher le graphique
    plt.show()
    print("Graphique généré à partir de la colonne : " + str(colonne))
   
def msgStartGraph():
    """Afficher le message de démarrage de génération de graphique"""
    time.sleep(5)
    print(graphStart)

# PROGRAMME PRINCIPAL

print(start)
msgStartGraph()
graphParColonne(arating)
#Supprime chaque ligne sans aucun review utilisateur + les lignes contenant des valeurs manquantes.
games = games[games[urated] > 0]
games = games.dropna(axis=0)
print("Dataset filtré")
msgStartGraph()
graphParColonne(arating)

"""
# Initialiser le modèle avec 2 paramètres -- nombre de clusters et random state.
kmeans_model = KMeans(n_clusters=5, random_state=1)
# Seulement les colonnes numériques de games.
good_columns = games._get_numeric_data()
# Adapter le modèle en utilisant les bonnes colonnes.
kmeans_model.fit(good_columns)
# Obtenir les labels des clusters.
labels = kmeans_model.labels_
"""

# Afficher les noms de colonnes du DataFrame games.
#print("Colonne : " + games.columns)
# Afficher les dimensions du Dataframe ex: 81312 lignes et 20 colonnes)
#print("Dimensions : " + str(games.shape))
# Afficher la première ligne du DataFrame games avec des notes de 0.
# La méthode .iloc sur des dataframes nous permet d'indexer par position.
#print(games[games[arating] == 0].iloc[0])
# Afficher la première ligne de tous les jeux de sociétés dont la note est supérieure à 0.
#print(games[games[arating] > 0].iloc[0])