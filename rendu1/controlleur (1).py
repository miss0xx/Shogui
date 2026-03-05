# -*- coding: utf-8 -*-
"""
Auteurs:
    - AIT SALEM Nora
    - BOUSSAA Thiziri
"""

"""
CONTROLEUR

Ce fichier fait le lien entre le modèle 
et la vue.

C'est le programme principal.
"""

import modele
import ihm

# INITIALISATION
modele.initialiser_grille()
modele.placer_pions_depart()

ihm.dessiner_grille()
ihm.dessiner_pions()

# GESTION DU DEPLACEMENT

piece_selectionnee = None

def clic_souris(event):
    """
    Gestion du clic souris.
    """

    global piece_selectionnee

    #On cacule le numéros de case avec la postion souris
    colonne = event.x // modele.TAILLE_CASE
    ligne = event.y // modele.TAILLE_CASE

    # Vérifier si clic dans la grille
    if ligne < 0 or ligne >= modele.NB_LIGNES:
        piece_selectionnee = None
        #Clic dehors -> On annule la sélection
        return

    if colonne < 0 or colonne >= modele.NB_COLONNES:
        piece_selectionnee = None
        #Clic dehors -> On annule la sélection
        return

    # Si aucune pièce sélectionnée (si c'est le premier clic)
    if piece_selectionnee is None:

        #On vérifie si la case contient une pièce
        if modele.grille[ligne][colonne] != 0:
            piece_selectionnee = (ligne, colonne)

    else:
        # Déplacement

        ancienne_ligne, ancienne_colonne = piece_selectionnee

        # Déplacer uniquement si case vide
        if modele.grille[ligne][colonne] == 0:

            modele.grille[ligne][colonne] = modele.grille[ancienne_ligne][ancienne_colonne]
            modele.grille[ancienne_ligne][ancienne_colonne] = 0

        # Si clic hors grille → reposition automatique
        piece_selectionnee = None

        ihm.dessiner_pions()

# Lier la souris
ihm.canvas.bind("<Button-1>", clic_souris)

# Lancer l'application
ihm.window.mainloop()
