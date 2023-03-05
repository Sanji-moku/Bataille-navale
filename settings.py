import pygame, sys, random, string

# Couleurs
BACKGROUND = (38, 123, 168)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (234, 0, 0)

# Font
FONT = 'PoetsenOne-Regular.ttf'

# Cellules
CELL_SIZE = 60
CELL_NUMBER = 10
BORDER = 10

# Taille d'affichage
SCREEN_SIZE = CELL_NUMBER * CELL_SIZE + (BORDER * CELL_NUMBER + BORDER) # 710px * 710px

# 2D Array # Cette grille renseigne la position de tous les navires dans un tableau de 2 Dimension et de taille 10 x 10
grid = [[0 for i in range(CELL_NUMBER)] for i in range(CELL_NUMBER)]

# VALEURS DANS LES CASES DU 2D ARRAY #
'''
0 => VIDE 
1 => NAVIRE PAS TOUCHE
2 => NAVIRE TOUCHE
4 => TIR RATE
'''

