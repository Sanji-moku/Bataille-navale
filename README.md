# Jeu de la bataille navale Solo

## Règles du jeu
Cette Bataille Navale est un jeu à un joueur. 
Le but de ce jeu est de trouver l’emplacement de chaque navire dans une flotte. 
Le jeu est composé d’une grille de taille 10 par 10 selon le plateau de jeu traditionnel représentant une portion de mer divisée en cellules carrées. 

Au sein de cette grille est cachée une flotte composée de : 
- 1 Croiseur de taille 4 
- 2 Escorteurs de taille 3 
- 3 Torpilleurs de taille 2 
- 4 Sous-marins de taille 1 

## La flotte est positionnée de manière aléatoire selon les crtières suivants:

- Chaque navire occupe des cellules contiguës sur la grille.
- Les navires sont positionnés soit horizontalement, soit verticalement. 
- Les navires ne peuvent pas se toucher (même en diagonale).

## Plateau de jeu
Grille de taille 10x10 dont les lignes sont numérotées de 1 à 10 et les colonnes de A à J
<img src="https://user-images.githubusercontent.com/80407460/222981363-f942b821-5821-4ea5-9cdf-2a4c3813471b.png" width="400">

### Case intacte
Les cases noires avec leur emplacement signifient qu'elles n'ont pas encore été découverte
<img align="left" width="50" height="50" src="https://user-images.githubusercontent.com/80407460/222981846-88c0cb95-71bd-4d45-8bb0-de6bbc627a32.png">
<br clear="left"/>


### Case tir tombe à l'eau
Les cases avec croix noire signifient qu'un tir a été lancé mais est tombée à l'eau
<img align="left" width="50" height="50" src="https://user-images.githubusercontent.com/80407460/222981553-64fac3aa-116d-4d08-8792-80cd1b863245.png">
<br clear="left"/>

### Case cible touchée
Les cases rouges avec croix signifient qu'un navire a été touchée
<img align="left" width="50" height="50" src="https://user-images.githubusercontent.com/80407460/222982029-906011ff-d62e-4ca0-bc3d-060959598327.png">
<br clear="left"/>

## Installation

Dézipper le dépôt git ou bien cloner le dépôt

    $ https://github.com/Sanji-moku/Bataille-navale.git

Installer les dépendances python

    $ python -m pip install -r requirements.txt
    
Lancer le jeu

    $ python main.py
    
Jouer !

