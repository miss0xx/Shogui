# -*- coding: utf-8 -*-
"""
Auteurs:
    - AIT SALEM Nora
    - BOUSSAA Thiziri
"""

"""
MODELE

Ce fichier contient uniquement les données
et les fonctions qui modifient ces données.

"""
# CONSTANTES DU PLATEAU

NB_LIGNES = 9
NB_COLONNES = 9
def av_c1(x , y):
    return (x+1 , y)
def av_cn(x , y , n):
    return (x+n , y)
def ar_c1(x , y):
    return (x-1 , y)
def ar_cn(x , y ,n ):
    return (x - n , y)
def g1(x , y):
    return (x , y - 1)
def gn(x , y , n):
    return (x , y - n )
def d1(x , y):
    return (x  , y + 1)
def dn(x , y ,n ):
    return (x , y +n)
def di_hd1(x , y ):
    return (x-1 , y+1)
def di_hg1(x , y ):
    return(x-1 , y -1)
def di_hdn(x , y , n):
    return (x-n , y+n)
def di_hgn(x , y , n):
    return(x-n , y -n)
def di_bd1(x , y ):
    return (x+1 , y+1)
def di_bg1(x , y):
    return(x+1 , y -1)
def di_bdn(x , y , n):
    return (x+n , y+n)
def di_bgn(x , y , n):
    return(x+n , y -n)
def cavd1(x , y ):
    return (x-2 , y+1)
def cavd1(x , y ):
    return(x-2 , y -1)



# Taille d'une case (en pixels)
TAILLE_CASE = 60

# DONNEES DU JEU
# La grille est représentée par une liste 2D
#--> une liste de lignes 
# 0 = case vide
# 1 = pion joueur 1
# 2 = pion joueur 2

grille = []

def initialiser_grille():
    """
    Initialise la grille avec des cases vides
    """
    global grille
    grille = []

    for i in range(NB_LIGNES):
        ligne = []
        for j in range(NB_COLONNES):
            ligne.append(0)
        grille.append(ligne)

def placer_pions_depart():
    """
    Place quelques pions au départ
    """

    # Exemple:
    # ligne 2 -> joueur 1
    # ligne 6 -> joueur 2

    for j in range(NB_COLONNES):
        grille[2][j] = 1
        grille[6][j] = 2
 
