import pandas as pd
import matplotlib.pyplot as plt
import time
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 00:02:51 2023

@author: xhackax47
"""

# Variables

affichageInfos = "Affichage de certaines informations concernant le DataSet utilisé : "
arating = "average_rating"
delaiStartGraph = 2.5
delaiStartFiltre = 3.5
graphStart = "Génération du graphique en cours..."
graph2Start = "Génération du graphique nuage en cours..."
harating = "bayes_average_rating"
name = "name"
typec = "type"
urated = "users_rated"
target = arating

# Fonctions


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
    # Obtenir toutes les colonnes du DataFrame games.
    columns = dataset.columns.tolist()
    # Filtrer les colonnes pour supprimer celles que nous ne voulons pas.
    columns = [c for c in columns if c not in [harating, arating, typec, name]]
    time.sleep(delaiStartFiltre)
    print("Dataset filtré")
    return dataset

def corrDataModel(dataset, colonne):
    """Afficher les corrélations de la colonne"""
    print("Affichage des corrélations pour la colonne : " + colonne)
    print(dataset.corr(numeric_only=True)[colonne])

def graphParColonne(dataset, colonne):
    """Génération d'un graphique à partir d'une colonne."""
    time.sleep(delaiStartGraph)
    print(graphStart)
    # Histogramme de toutes les notes de la colonne.
    plt.hist(dataset[colonne])
    # Afficher le graphique
    plt.show()
    print("Graphique généré à partir de la colonne : " + str(colonne))


def graphDataModel(dataset):
    """Initialiser le modèle de données, les clusters et afficher le graphique résultant"""
    time.sleep(delaiStartGraph)
    print(graph2Start)
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
    
def entrainement(dataset):
    """Séparer le dataset en 2 sets et créer le modèle de régression linéaire et l'entraîner avec le datasets train"""
    # Générer le set de training. Fixer random_state pour répliquer lé resultats ultérieurement.
    train = dataset.sample(frac=0.8, random_state=1)
    # Sélectionner tout ce qui n'est pas dans le set de training et le mettre dans le set de test.
    test = dataset.loc[~dataset.index.isin(train.index)]
    print("Dataset séparé en 2, train et test")
    # Afficher les dimensions des 2 sets.
    print("Dimension DataSet d'entraînement = " + str(train.shape))
    print("Dimension DataSet de test = " + str(test.shape))
    # Initialiser la classe du modèle.
    model = LinearRegression()
    # Obtenir toutes les colonnes du DataFrame.
    columns = dataset.columns.tolist()
    # Filtrer les colonnes pour supprimer celles que nous ne voulons pas.
    columns = [c for c in columns if c not in [harating, arating, typec, name]]
    # Adapter le modèle aux données d'entrainement
    model.fit(train[columns], train[target])
    print("Calcul du taux d'erreur des prédictions de notre modèle")
    # Générer des prédictions pour le set de test.
    predictions = model.predict(test[columns])
    # Calculer l'erreur entre nos prédictions et les valeurs réelles que nous connaissons.
    erreur = mean_squared_error(predictions, test[target])
    print("Taux d'erreur = " + str(erreur))