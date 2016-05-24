# This Python file uses the following encoding: utf-8
"""
Morpion en 3 dimensions avec une IA utilisant l'algorithme Minimax implémenté
Copyright (C) 2015  Guillaume Augustoni, Leo Henriot, Raphael Chevalier et Enzo cabezas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>."""
from copy import *
from random import randrange
from plateau import *

class IA():
    """Classe de base qui nous permet de définir les différentes fonctions
    que toutes les IA doivent posséder. Cette classe n'est pas faite pour être
    utilisé directement mais seulement en la héritant à une autre classe
    programmeur : Guillaume"""
    def __init__(self, t_Plateau):
        """Toutes les IA utilisent ces fonctions on les assigne donc ici"""
        self.p_Plateau = t_Plateau
    def meilleurMouvement(self):
        """Cette fonction doit être implémenté dans chaque IA si elle ne l'est pas
        il y a erreur """
        self.Plateau = Plateau(self.p_Plateau.render, self.p_Plateau.loader, graphismes_actifs = False)
        self.Plateau.mouvementjoues = deepcopy(self.p_Plateau.mouvementjoues)
        self.Plateau.tourBlanc = self.p_Plateau.tourBlanc
        self.Plateau.liste = deepcopy(self.p_Plateau.liste)
class IA_Difficile(IA):
    """Cette IA utilise l'algorithme minimax pour choisir le meilleur mouvement
    elle hérite les fonctions nécessaires a son fonctionement de IA
    programmeur : Guillaume"""
    def __init__(self, Plateau):
        IA.__init__(self, Plateau)
    def monminimaxamoi(self):
        """L'implémentation de l'algorithme minimax.
        Elle renvoit une valeur pour chaque tableau"""
        mouvements = self.Plateau.mouvementPossible()
        #si on ne peut plus jouer sur un tableau et qu'il n'y a pas eu de
        #victoires c'est qu'il y a égalité le tableau vaut donc 0
        if mouvements == []:
            return 0
        #On parcoure tous les mouvements possibles, on les joue
        #en placant les états qui en résultent dans le tableau etats
        valeursEtats = []
        for mouvement in mouvements:
            #on copie le tableau de base pour ne pas le modifier
            self.Plateau.jouerMouvement(mouvement)
            #on joue le mouvemnt sur le tableau temporaire et on regarde s'il y a
            #victoire en revoyant
            if self.Plateau.testVictoire() != 0:
                valeur = self.Plateau.testVictoire()
                self.Plateau.annulerMouvement()
                return valeur
            else:
                valeursEtats.append(self.monminimaxamoi())
            self.Plateau.annulerMouvement()
        #La valeur
        if self.Plateau.tourBlanc:
            return max(valeursEtats)
        else:
            return min(valeursEtats)

    def meilleurMouvement(self):
        IA.meilleurMouvement(self)
        mouvements=self.Plateau.mouvementPossible()
        print(mouvements)
        valeurs = [None for i in range(9)]
        valeurajouer = None
        for mouvement in mouvements:
            self.Plateau.jouerMouvement(mouvement)
            if self.Plateau.testVictoire() != 0:
                print(self.Plateau)
                valeurajouer = i
            self.Plateau.annulerMouvement()
        if valeurajouer == None:
            for mouvement in mouvements:
                self.Plateau.jouerMouvement(mouvement)
                valeurs[mouvement] = self.monminimaxamoi()
                self.Plateau.annulerMouvement()
        print("valeur")
        print(valeurs)
        print(valeurajouer)
        if valeurajouer == None and self.Plateau.tourBlanc:
            valeurajouer = valeurs.index(max(valeurs))
        elif  valeurajouer == None :
            valeurajouer = valeurs.index(min([x for x in valeurs if x != None]))
        return valeurajouer
class IA_Moyenne(IA):
    def __init__(self, Plateau):
        IA.__init__(self, Plateau)
    def meilleurMouvement(self):
        IA.meilleurMouvement(self)
        temp=self.Plateau.mouvementPossible()
        valeurs = [None for i in range(9)]
        valeurajouer = None
        for mouvement in temp:
            self.Plateau.jouerMouvement(mouvement)
            if self.Plateau.testVictoire() != 0:
                valeurajouer = mouvement
            self.Plateau.annulerMouvement()
        if valeurajouer == None:
            valeurajouer = temp[randrange(len(temp))]
        return valeurajouer
class IA_Facile(IA):
    def __init__(self, Plateau):
        IA.__init__(self, Plateau)
    def meilleurMouvement(self):
        IA.meilleurMouvement(self)
        return self.Plateau.mouvementPossible()[randrange(len(self.Plateau.mouvementPossible()))]
class bloc_IA():
    def __init__(self, Plateau):
        self.IA = IA_Facile(Plateau)
