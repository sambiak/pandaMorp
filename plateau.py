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
from panda3d.core import Point3, LPoint3
from direct.showbase import DirectObject
MARRON = (0.5,0.25,0,1)
BLACK = (0, 0, 0, 1)


def position(i):
    return LPoint3(-3+3*(i%3),-3+3*(i//3),0)
class Plateau(DirectObject.DirectObject):
    def __init__(self,render,loader, graphismes_actifs = True, tourBlanc = True):
        self.liste = [[0 for i in range(3)]for i in range(3)]
        self.tours = [None for i in range(9)]
        self.pions = [None for i in range(9)]
        self.mouvementjoues = []
        self.graphismes_actifs = graphismes_actifs
        self.tourBlanc = tourBlanc
        self.loader = loader
        self.render = render
    def __str__(self):
        return "Test Victoire: " + self.testVictoire().__str__() + "\n Plateau: " + self.liste.__str__()
    def __testVictoire(self, Liste):
        if Liste[0][0] + Liste [0][1] + Liste [0][2] == 30:
            return 1
        elif Liste[0][0] + Liste [0][1] + Liste [0][2] == 3:
            return -1
        elif Liste[1][0] + Liste [1][1] + Liste [1][2] == 30:
            return 1
        elif Liste[1][0] + Liste [1][1] + Liste [1][2] == 3:
            return -1
        elif Liste[2][0] + Liste [2][1] + Liste [2][2] == 30:
            return 1
        elif Liste[2][0] + Liste [2][1] + Liste [2][2] == 3:
            return -1
        elif Liste[0][0] + Liste [1][0] + Liste [2][0] == 30:
            return 1
        elif Liste[0][0] + Liste [1][0] + Liste [2][0] == 3:
            return -1
        elif Liste[0][1] + Liste [1][1] + Liste [2][1] == 30:
            return 1
        elif Liste[0][1] + Liste [1][1] + Liste [2][1] == 3:
            return -1
        elif Liste[0][2] + Liste [1][2] + Liste [2][2] == 30:
            return 1
        elif Liste[0][2] + Liste [1][2] + Liste [2][2] == 3:
            return -1
        elif Liste[0][0] + Liste [1][1] + Liste [2][2] == 30:
            return 1
        elif Liste[0][0] + Liste [1][1] + Liste [2][2] == 3:
            return -1
        elif Liste[0][2] + Liste [1][1] + Liste [2][0] == 30:
            return 1
        elif Liste[0][2] + Liste [1][1] + Liste [2][0] == 3:
            return -1
        else:
            return 0
        print("Si ce texte s'affiche sur la console il y a un probleme avec le test de victoire")
    def testVictoire(self):
        return self.__testVictoire(self.liste)
    def mouvementPossible(self):
        temp = []
        for i in range(9):
            if self.liste[i//3][i%3] == 0:
                temp.append(i)
        return temp
    def reset(self):
        for i in range(9):
            if self.pions[i] is not None:
                self.pions[i].detachNode()
            self.liste[i//3][i%3] = 0
        self.mouvementjoues = []
        self.tourBlanc = True
    def jouerMouvement(self, mouvement):
        if self.testVictoire() == 0:
            if self.liste[mouvement // 3][mouvement %3] == 0:
                self.mouvementjoues.append(mouvement)
                self.afficherPion(mouvement, self.tourBlanc)
                if self.tourBlanc == False:
                    self.liste[mouvement//3][mouvement%3] = 1
                else:
                    self.liste[mouvement//3][mouvement%3] = 10
                self.tourBlanc = not self.tourBlanc
    def afficherPion(self, mouvement, tourBlanc):
        if self.graphismes_actifs:
            self.pions[mouvement] = self.loader.loadModel("torus")
            self.pions[mouvement].reparentTo(self.render)
            self.pions[mouvement].setScale(0.37465, 0.37465, 0.37465)
            if not tourBlanc:
                self.pions[mouvement].setColor(BLACK)
            self.pions[mouvement].setPos(position(mouvement))
    def chargerGraphismes(self):
        self.graphismes_actifs = True
        print(self.mouvementjoues)
        for i in range(9):#création des 9 tours
            self.tours[i] = self.loader.loadModel("bois")
            self.tours[i].reparentTo(self.render)
            self.tours[i].setScale(0.25, 0.25, 0.25) #Echelle
            self.tours[i].setColor(MARRON)
            self.tours[i].setPos(position(i))
        stockageTour = self.tourBlanc
        for i in range(len(self.mouvementjoues)):
            self.afficherPion(self.mouvementjoues[len(self.mouvementjoues)- 1 - i], stockageTour)
            stockageTour = not stockageTour

    def dechargerGraphismes(self):
        """Efface tous les tours présentes et les pions"""
        for tour in self.tours:
            if tour is not None:
                tour.detachNode()
        for pion in self.pions:
            if pion is not None:
                pion.detachNode()
        self.graphismes_actifs = False
    def annulerMouvement(self):
        dernierMouvement = self.mouvementjoues.pop()
        if self.graphismes_actifs:
            self.pions[dernierMouvement].detachNode()
        self.liste[dernierMouvement//3][dernierMouvement%3] = 0
        self.tourBlanc = not self.tourBlanc
