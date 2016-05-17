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

class IA():
    """Classe de base qui nous permet de définir les différentes fonctions
    que toutes les IA doivent posséder. Cette classe n'est pas faite pour être
    utilisé directement mais seulement en la héritant à une autre classe
    programmeur : Guillaume"""
    def __init__(self, testVictoire, mouvementPossible):
        """Toutes les IA utilisent ces fonctions on les assigne donc ici"""
        self.testVictoire = testVictoire
        self.mouvementPossible = mouvementPossible
    def meilleurMouvement(self, tableau, tourBlanc):
        """Cette fonction doit être implémenté dans chaque IA si elle ne l'est pas
        il y a erreur """
        pass
class IA_Difficile(IA):
    """Cette IA utilise l'algorithme minimax pour choisir le meilleur mouvement
    elle hérite les fonctions nécessaires a son fonctionement de IA
    programmeur : Guillaume"""
    def __init__(self, testVictoire, mouvementPossible):
        IA.__init__(self, testVictoire, mouvementPossible)
    def monminimaxamoi(self, tableau,tourBlanc):
        """L'implémentation de l'algorithme minimax.
        Elle renvoit une valeur pour chaque tableau"""
        etats = []
        mouvements = self.mouvementPossible(tableau)
        #si on ne peut plus jouer sur un tableau et qu'il n'y a pas eu de
        #victoires c'est qu'il y a égalité le tableau vaut donc 0
        if mouvements == []:
            return 0
        #On parcoure tous les mouvements possibles, on les joue
        #en placant les états qui en résultent dans le tableau etats
        for mouvement in mouvements:
            #on copie le tableau de base pour ne pas le modifier
            etats.append(deepcopy(tableau))
            #on joue le mouvemnt sur le tableau temporaire et on regarde s'il y a
            #victoire en revoyant
            if tourBlanc:
                etats[len(etats)-1] [mouvement//3][mouvement%3] = 10
                if self.testVictoire(etats[len(etats)-1]) != 0:
                    return 1
            else:
                etats[len(etats)-1] [mouvement//3][mouvement%3] = 1
                if self.testVictoire(etats[len(etats)-1]) != 0:

                    return -1
        valeursEtats = []
        for x in etats:
            valeursEtats.append(self.monminimaxamoi(x, not tourBlanc))
        if tourBlanc:
            return max(valeursEtats)
        else:
            return min(valeursEtats)

    def meilleurMouvement(self, tableau, tourBlanc):
        print(tableau)
        temp=self.mouvementPossible(tableau)
        etat=[None for i in range(9)]
        valeurs = [None for i in range(9)]
        valeurajouer = None
        for i in temp:
            etat[i] = deepcopy(tableau)
            if tourBlanc:
                etat[i] [i//3][i%3] = 10
                if self.testVictoire(etat[i]) != 0:
                    valeurajouer = i
            else:
                etat[i] [i//3][i%3] = 1
                if self.testVictoire(etat[i]) != 0:
                    valeurajouer = i
        if valeurajouer == None:
            for i in etat:
                if i is not None:
                    temp2 = self.monminimaxamoi(i, not tourBlanc)
                    valeurs[etat.index(i)] = temp2
        print("fin")
        print(etat)
        print(valeurs)
        print(valeurajouer)
        if valeurajouer == None and tourBlanc:
            valeurajouer = valeurs.index(max(valeurs))
        elif  valeurajouer == None :
            valeurajouer = valeurs.index(min([x for x in valeurs if x != None]))
        return valeurajouer
class IA_Moyenne(IA):
    def __init__(self, testVictoire, mouvementPossible):
        IA.__init__(self, testVictoire, mouvementPossible)
    def meilleurMouvement(self, tableau, tourBlanc):
        print(tableau)
        temp=self.mouvementPossible(tableau)
        etat=[None for i in range(9)]
        valeurs = [None for i in range(9)]
        valeurajouer = None
        for i in temp:
            etat[i] = deepcopy(tableau)
            if tourBlanc:
                etat[i] [i//3][i%3] = 10
                if self.testVictoire(etat[i]) != 0:
                    valeurajouer = i
            else:
                etat[i] [i//3][i%3] = 1
                if self.testVictoire(etat[i]) != 0:
                    valeurajouer = i
        if valeurajouer == None:
            valeurajouer = temp[randrange(len(temp))]
        return valeurajouer
class IA_Facile(IA):
    def __init__(self, testVictoire, mouvementPossible):
        IA.__init__(self, testVictoire, mouvementPossible)
    def meilleurMouvement(self, tableau, tourBlanc):
        mouvements = self.mouvementPossible(tableau)
        return mouvements[randrange(len(mouvements))]
