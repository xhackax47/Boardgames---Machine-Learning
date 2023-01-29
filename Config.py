import pandas as pd
import matplotlib.pyplot as plt
import time
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 00:02:51 2023

@author: samy_
"""

# Variables

msgStart = "INITIALISATION ET DEMARRAGE DU PROGRAMME PRINCIPAL"
msgEnd = "FIN DU PROGRAMME PRINCIPAL"
graphStart = "Génération du graphique en cours..."
affichageInfos = "Affichage de certaines informations concernant le DataSet utilisé : "
arating = "average_rating"
urated = "users_rated"
delaiStartGraph = 2.5
# Lire les données.

# Fonctions


def msgStartGraph():
    """Afficher le message de démarrage de génération de graphique"""
    time.sleep(delaiStartGraph)
    print(graphStart)


def afficherInfosDataSet(dataset):
    """Affichier infos sur le dataset"""
    time.sleep(1)
    print(affichageInfos)
    # Afficher les noms de colonnes du DataFrame games.
    print("Colonne : " + dataset.columns)
    # Afficher les dimensions du Dataframe ex: 81312 lignes et 20 colonnes)
    print("Dimensions : " + str(dataset.shape))
    # Afficher la première ligne du DataFrame games avec des notes de 0.
    # La méthode .iloc sur des dataframes nous permet d'indexer par position.
    print(dataset[dataset[arating] == 0].iloc[0])
    # Afficher la première ligne de tous les jeux de sociétés dont la note est supérieure à 0.
    print(dataset[dataset[arating] > 0].iloc[0])


def filtreDatas(dataset):
    """Supprime chaque ligne sans aucun review utilisateur + les lignes contenant des valeurs manquantes."""
    dataset = dataset[dataset[urated] > 0]
    dataset = dataset.dropna(axis=0)
    time.sleep(delaiStartGraph)
    print("Dataset filtré")
    return dataset

def corrDataModel(dataset, colonne):
    """Afficher les corrélations de la colonne"""
    print(dataset.corr(numeric_only=True)[colonne])

def graphParColonne(dataset, colonne):
    """Génération d'un graphique à partir d'une colonne."""
    msgStartGraph()
    # Histogramme de toutes les notes de la colonne.
    plt.hist(dataset[colonne])
    # Afficher le graphique
    plt.show()
    print("Graphique généré à partir de la colonne : " + str(colonne))


def graphDataModel(dataset):
    """Initialiser le modèle de données, les clusters et afficher le graphique résultant"""
    # Initialiser le modèle avec 2 paramètres -- nombre de clusters et random state.
    kmeans_model = KMeans(n_clusters=5, random_state=1, n_init="auto")
    # Seulement les colonnes numériques de games.
    good_columns = dataset._get_numeric_data()
    # Adapter le modèle en utilisant les bonnes colonnes.
    kmeans_model.fit(good_columns)
    # Obtenir les labels des clusters.
    labels = kmeans_model.labels_
    # Créer un modèle PCA.
    pca_2 = PCA(2)
    # adapter le modèle PCA aux colonnes numériques précédentes.
    plot_columns = pca_2.fit_transform(good_columns)
    # Faire un graphique à nuage de points pour chaque type de jeux de société, à partir des clusters.
    plt.scatter(x=plot_columns[:, 0], y=plot_columns[:, 1], c=labels)
    # Afficher le graphique.
    plt.show()
