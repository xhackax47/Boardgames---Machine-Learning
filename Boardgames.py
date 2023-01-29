from Config import *


# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 12:13:23 2023

@author: xhackax47
"""
# PROGRAMME PRINCIPAL
games = pd.io.parsers.read_csv("datasets/games.csv")
print(msgStart)
afficherInfosDataSet(games)
graphParColonne(games, arating)
games = filtreDatas(games)
graphParColonne(games, arating)
graphDataModel(games)
corrDataModel(games, arating)
print(msgEnd)