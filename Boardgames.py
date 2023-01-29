from Config import *


# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 12:13:23 2023

@author: xhackax47
"""
dataset = pd.io.parsers.read_csv("datasets/games.csv")
# PROGRAMME PRINCIPAL
print("INITIALISATION ET DEMARRAGE DU PROGRAMME PRINCIPAL")
boardgamesStart(dataset)
print("FIN DU PROGRAMME PRINCIPAL")