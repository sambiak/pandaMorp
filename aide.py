# This Python file uses the following encoding: utf-8
"""
Morpion en 3 dimensions avec une IA utilisant l'algorithme Minimax implémenté
Copyright (C) 2015  Guillaume Augustoni, leo

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

        return 21
    def __init__(self):
        ShowBase.__init__(self)

        self.camera.setPosHpr(0, -12, 8, 0, -35, 0)
        self.disableMouse()
        self.tableau = [[0 for i in range(3)]for i in range(3)]
        for i in range(9):
            self.environ = self.loader.loadModel("bois")
            self.environ.reparentTo(self.render)
            self.environ.setScale(0.25, 0.25, 0.25) #Echelle
            self.environ.setColor(MARRON)
            self.environ.setPos(position(i))
        self.environ = [None for i in range(9)]
        self.tourBlanc = True
        self.accept('1',lambda x : addCercle(0))
        self.accept('2',self.addCercle1)
        self.accept('3',self.addCercle2)
        self.accept('4',self.addCercle3)
        self.accept('5',self.addCercle4)
        self.accept('6',self.addCercle5)
        self.accept('7',self.addCercle6)
        self.accept('8',self.addCercle7)
        self.accept('9',self.addCercle8)
        self.accept('r',self.reset)
        self.accept('t',self.test)

    def reset(self):
        for i in range(9):
            if self.environ[i] is not None:
                self.environ[i].detachNode()
            self.tableau[i%3][i//3] = 0


    def addCercle(self, i):
        if self.testVictoire(self.tableau) == 0:
            if self.tableau[i % 3][i //3] == 0:
                self.environ[i] = self.loader.loadModel("torus")
                self.environ[i].reparentTo(self.render)
                self.environ[i].setScale(0.37465, 0.37465, 0.37465)
                if self.tourBlanc == False:
                    self.tableau[i%3][i//3] = 1
                    self.environ[i].setColor(BLACK)
                else:
                    self.tableau[i%3][i//3] = 10
                self.environ[i].setPos(position(i))
                self.tourBlanc = not self.tourBlanc
    def addCercle1(self):
        if self.testVictoire(self.tableau) == 0:
            if self.tableau[0][1] == 0:
                self.environ[1] = self.loader.loadModel("torus")
                self.environ[1].reparentTo(self.render)
                self.environ[1].setScale(0.37465, 0.37465, 0.37465)
                if self.tourBlanc == False:
                    self.environ[1].setColor(BLACK)
                    self.tableau[0][1] = 1
                else:
                    self.tableau[0][1] = 10
                self.environ[1].setPos(position(1))
                self.tourBlanc = not self.tourBlanc
    def addCercle2(self):
        if self.testVictoire(self.tableau) == 0:
            if self.tableau[0][2] == 0:
                self.environ[2] = self.loader.loadModel("torus")
                self.environ[2].reparentTo(self.render)
                self.environ[2].setScale(0.37465, 0.37465, 0.37465)
                if self.tourBlanc == False:
                    self.environ[2].setColor(BLACK)
                    self.tableau[0][2] = 1
                else:
                    self.tableau[0][2] = 10
                self.environ[2].setPos(position(2))
                self.tourBlanc = not self.tourBlanc
    def addCercle3(self):
        if self.testVictoire(self.tableau) == 0:
            if self.tableau[1][0] == 0:
                self.environ[3] = self.loader.loadModel("torus")
                self.environ[3].reparentTo(self.render)
                self.environ[3].setScale(0.37465, 0.37465, 0.37465)
                if self.tourBlanc == False:
                    self.environ[3].setColor(BLACK)
                    self.tableau[1][0] = 1
                else:
                    self.tableau[1][0] = 10
                self.environ[3].setPos(position(3))
                self.tourBlanc = not self.tourBlanc
    def addCercle4(self):
        if self.testVictoire(self.tableau) == 0:
            if self.tableau[1][1] == 0:
                self.environ[4] = self.loader.loadModel("torus")
                self.environ[4].reparentTo(self.render)
                self.environ[4].setScale(0.37465, 0.37465, 0.37465)
                if self.tourBlanc == False:
                    self.environ[4].setColor(BLACK)
                    self.tableau[1][1] = 1
                else:
                    self.tableau[1][1] = 10
                self.environ[4].setPos(position(4))
                self.tourBlanc = not self.tourBlanc
    def addCercle5(self):
        if self.testVictoire(self.tableau) == 0:
            if self.tableau[1][2] == 0:
                self.environ[5] = self.loader.loadModel("torus")
                self.environ[5].reparentTo(self.render)
                self.environ[5].setScale(0.37465, 0.37465, 0.37465)
                if self.tourBlanc == False:
                    self.environ[5].setColor(BLACK)
                    self.tableau[1][2] = 1
                else:
                    self.tableau[1][2] = 10
                self.environ[5].setPos(position(5))
                self.tourBlanc = not self.tourBlanc
    def addCercle6(self):
        if self.testVictoire(self.tableau) == 0:
            if self.tableau[2][0] == 0:
                self.environ[6] = self.loader.loadModel("torus")
                self.environ[6].reparentTo(self.render)
                self.environ[6].setScale(0.37465, 0.37465, 0.37465)
                if self.tourBlanc == False:
                    self.environ[6].setColor(BLACK)
                    self.tableau[2][0] = 1
                else:
                    self.tableau[2][0] = 10
                self.environ[6].setPos(position(6))
                self.tourBlanc = not self.tourBlanc
    def addCercle7(self):
        if self.testVictoire(self.tableau) == 0:
            if self.tableau[2][1] == 0:
                self.environ[7] = self.loader.loadModel("torus")
                self.environ[7].reparentTo(self.render)
                self.environ[7].setScale(0.37465, 0.37465, 0.37465)
                if self.tourBlanc == False:
                    self.environ[7].setColor(BLACK)
                    self.tableau[2][1] = 1
                else:
                    self.tableau[2][1] = 10
                self.environ[7].setPos(position(7))
                self.tourBlanc = not self.tourBlanc
    def addCercle8(self):
        if self.testVictoire(self.tableau) == 0:
            if self.tableau[2][2] == 0:
                self.environ[8] = self.loader.loadModel("torus")
                self.environ[8].reparentTo(self.render)
                self.environ[8].setScale(0.37465, 0.37465, 0.37465)
                if self.tourBlanc == False:
                    self.environ[8].setColor(BLACK)
                    self.tableau[2][2] = 1
                else:
                    self.tableau[2][2] = 10
                self.environ[8].setPos(position(8))
                self.tourBlanc = not self.tourBlanc
    def mouvementPossible(self, table):
        temp = []
        for i in range(9):
            if table[i//3][i%3] == 0:
                temp.append(i)
        return temp
    """def test(self):
        print("Mouvement possible")
        print(self.mouvementPossible(self.tableau))
        print(self.tableau)
        temp3 = self.mouvementPossible(self.tableau)
        mouvgagnant=[]
        for i in temp3:
            temp2=[[y for y in w] for w in self.tableau]
            if self.tourBlanc:
                temp2[i//3][i%3]=10
            else:
                temp2[i//3][i%3]=1
            if self.testVictoire(temp2) is not 0:
                mouvgagnant.append(i)
        if len(mouvgagnant) is not 0:

            var = mouvgagnant[randrange(len(mouvgagnant))]
            if var == 0:
                self.addCercle0()
            elif var == 1:
                self.addCercle1()
            elif var == 2:
                self.addCercle2()
            elif var == 3:
                self.addCercle3()
            elif var == 4:
                self.addCercle4()
            elif var == 5:
                self.addCercle5()
            elif var == 6:
                self.addCercle6()
            elif var == 7:
                self.addCercle7()
            elif var == 8:
                self.addCercle8()
        elif len(self.mouvementPossible(self.tableau)) is not 0:

            var = self.mouvementPossible(self.tableau)[randrange(len(self.mouvementPossible(self.tableau)))]
            if var == 0:
                self.addCercle0()
            elif var == 1:
                self.addCercle1()
            elif var == 2:
                self.addCercle2()
            elif var == 3:
                self.addCercle3()
            elif var == 4:
                self.addCercle4()
            elif var == 5:
                self.addCercle5()
            elif var == 6:
                self.addCercle6()
            elif var == 7:
                self.addCercle7()
            elif var == 8:
                self.addCercle8()"""
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
                        print("valeur a jouer")
                        print(i)
                else:
                    etat[i] [i//3][i%3] = 1
                    if self.testVictoire(etat[i]) != 0:
                        valeurajouer = i
                        print("valeur a jouer")
                        print(i)
            if valeurajouer == None:
                for i in etat:
                    if i is not None:
                        temp2 = self.monminimaxamoi(i, not self.tourBlanc)
                        valeurs[etat.index(i)] = temp2
                        print(i)
                        print(temp2)

            print("fin")
            print(etat)
            print(valeurs)
            print(valeurajouer)
            if valeurajouer == None and self.tourBlanc:
                valeurajouer = valeurs.index(max(valeurs))
            elif  valeurajouer == None :
                valeurajouer = valeurs.index(min([x for x in valeurs if x != None]))
            if valeurajouer == 0:
                self.addCercle0()
            elif valeurajouer == 1:
                self.addCercle1()
            elif valeurajouer == 2:
                self.addCercle2()
            elif valeurajouer == 3:
                self.addCercle3()
            elif valeurajouer == 4:
                self.addCercle4()
            elif valeurajouer == 5:
                self.addCercle5()
            elif valeurajouer == 6:
                self.addCercle6()
            elif valeurajouer == 7:
                self.addCercle7()
            elif valeurajouer == 8:
                self.addCercle8()




app = MyApp()
app.run()
