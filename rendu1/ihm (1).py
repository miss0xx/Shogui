# -*- coding: utf-8 -*-
"""
Auteurs:
    - AIT SALEM Nora
    - BOUSSAA Thiziri
"""

"""
IHM (Interface Homme Machine)

Ce fichier contient uniquement l'affichage
graphique.
"""

import tkinter as tk
import modele

# Fenêtre principale
window = tk.Tk()
window.title("Shogi - Rendu 1")

# Canvas principal
canvas = tk.Canvas(
    window,
    width=modele.NB_COLONNES * modele.TAILLE_CASE,
    height=modele.NB_LIGNES * modele.TAILLE_CASE,
    bg="beige"
)

canvas.pack()

def dessiner_grille():
    #Dessine les lignes du plateau.
    for i in range(modele.NB_LIGNES + 1):
        canvas.create_line(
            0,
            i * modele.TAILLE_CASE,
            modele.NB_COLONNES * modele.TAILLE_CASE,
            i * modele.TAILLE_CASE
        )
    #Dessine les colonnes du plateau.
    for j in range(modele.NB_COLONNES + 1):
        canvas.create_line(
            j * modele.TAILLE_CASE,
            0,
            j * modele.TAILLE_CASE,
            modele.NB_LIGNES * modele.TAILLE_CASE
        )

def dessiner_pions():
    """
    Dessine les pions en fonction
    des données du modèle.
    """

    canvas.delete("pion")

    for i in range(modele.NB_LIGNES):
        for j in range(modele.NB_COLONNES):

            if modele.grille[i][j] == 1:
                dessiner_un_pion(i, j, "black")

            elif modele.grille[i][j] == 2:
                dessiner_un_pion(i, j, "red")

def dessiner_un_pion(ligne, colonne, couleur):
    """
    Dessine un pion centré dans une case.
    """

    x1 = colonne * modele.TAILLE_CASE + 10
    y1 = ligne * modele.TAILLE_CASE + 10

    x2 = (colonne + 1) * modele.TAILLE_CASE - 10
    y2 = (ligne + 1) * modele.TAILLE_CASE - 10

    canvas.create_oval(x1, y1, x2, y2, fill=couleur, tags="pion")
