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

from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3, LPoint3
from random import randrange
from copy import *
from itertools import chain

MARRON = (0.5,0.25,0,1)
BLACK = (0, 0, 0, 1)

def position(i):
    return LPoint3(-3+3*(i%3),-3+3*(i//3),0)


class MyApp(ShowBase):

    def testVictoire(self, Liste):
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
    def __init__(self):
        ShowBase.__init__(self)
        self.camera.setPosHpr(0, -12, 8, 0, -35, 0)
        self.disableMouse()
        self.tableau = [[0 for i in range(3)]for i in range(3)]
        self.tours = [None for i in range(9)]
        self.chargerGraphismes()
        self.environ = [None for i in range(9)]
        self.tourBlanc = True
        self.accept('1',lambda : self.ajouterCercle(0))
        self.accept('2',lambda : self.ajouterCercle(1))
        self.accept('3',lambda : self.ajouterCercle(2))
        self.accept('4',lambda : self.ajouterCercle(3))
        self.accept('5',lambda : self.ajouterCercle(4))
        self.accept('6',lambda : self.ajouterCercle(5))
        self.accept('7',lambda : self.ajouterCercle(6))
        self.accept('8',lambda : self.ajouterCercle(7))
        self.accept('9',lambda : self.ajouterCercle(8))
        self.accept('r',self.reset)
        self.accept('t',self.test)

    def chargerGraphismes(self):
        for i in range(9):#création des 9 tours
            self.tours[i] = self.loader.loadModel("bois")
            self.tours[i].reparentTo(self.render)
            self.tours[i].setScale(0.25, 0.25, 0.25) #Echelle
            self.tours[i].setColor(MARRON)
            self.tours[i].setPos(position(i))
    def dechargerGraphismes(self):
        """Eface tous les tours présente et les pions"""
        for tour in self.tours:
            if tour is not None:
                tour.detachNode
        self.reset()
    def reset(self):
        for i in range(9):
            if self.environ[i] is not None:
                self.environ[i].detachNode()
            self.tableau[i//3][i%3] = 0
        self.tourBlanc = True
    def mouvementPossible(self, table):
        temp = []
        for i in range(9):
            if table[i//3][i%3] == 0:
                temp.append(i)
        return temp


    def ajouterCercle(self, i):
        if self.testVictoire(self.tableau) == 0:
            if self.tableau[i // 3][i %3] == 0:
                self.environ[i] = self.loader.loadModel("torus")
                self.environ[i].reparentTo(self.render)
                self.environ[i].setScale(0.37465, 0.37465, 0.37465)
                if self.tourBlanc == False:
                    self.tableau[i//3][i%3] = 1
                    self.environ[i].setColor(BLACK)
                else:
                    self.tableau[i//3][i%3] = 10
                self.environ[i].setPos(position(i))
                self.tourBlanc = not self.tourBlanc
    def monminimaxamoi(self, tableau,tourBlanc):
        etat= []
        temp = self.mouvementPossible(tableau)
        if temp == []:
            return 0
        for i in temp:
            etat.append(deepcopy(tableau))
            if tourBlanc:
                etat[len(etat)-1] [i//3][i%3] = 10
                if self.testVictoire(etat[len(etat)-1]) != 0:
                    return 1
            else:
                etat[len(etat)-1] [i//3][i%3] = 1
                if self.testVictoire(etat[len(etat)-1]) != 0:

                    return -1
        valeursEtats = []
        for x in etat:
            valeursEtats.append(self.monminimaxamoi(x, not tourBlanc))
        if tourBlanc:
            return max(valeursEtats)
        else:
            return min(valeursEtats)



    def test(self):
        print(self.tableau)
        if 0 in chain.from_iterable(self.tableau):
            temp=self.mouvementPossible(self.tableau)
            etat=[None for i in range(9)]
            valeurs = [None for i in range(9)]
            valeurajouer = None
            for i in temp:
                etat[i] = deepcopy(self.tableau)
                if self.tourBlanc:
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
                        temp2 = self.monminimaxamoi(i, not self.tourBlanc)
                        valeurs[etat.index(i)] = temp2

            print("fin")
            print(etat)
            print(valeurs)
            print(valeurajouer)
            if valeurajouer == None and self.tourBlanc:
                valeurajouer = valeurs.index(max(valeurs))
            elif  valeurajouer == None :
                valeurajouer = valeurs.index(min([x for x in valeurs if x != None]))
            self.ajouterCercle(valeurajouer)




app = MyApp()
app.run()
