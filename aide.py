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
from itertools import chain
from random import randrange
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3, LPoint3
from direct.showbase import DirectObject
from IA import *
from menus import Menu
from audio import AudioManager
from plateau import *




class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.camera.setPosHpr(0, -12, 8, 0, -35, 0)
        self.disableMouse()
        self.tourBlanc = True
        self.Plateau = Plateau(self.render, self.loader)
        self.IA = bloc_IA(self.Plateau)
        self.son = AudioManager(self.loader)
        self.menu = Menu(self.loader,self.Plateau , self.son, self.IA)
        #mise en place des raccourcis
        self.accept('1',lambda : self.Plateau.jouerMouvement(0))
        self.accept('2',lambda : self.Plateau.jouerMouvement(1))
        self.accept('3',lambda : self.Plateau.jouerMouvement(2))
        self.accept('4',lambda : self.Plateau.jouerMouvement(3))
        self.accept('5',lambda : self.Plateau.jouerMouvement(4))
        self.accept('6',lambda : self.Plateau.jouerMouvement(5))
        self.accept('7',lambda : self.Plateau.jouerMouvement(6))
        self.accept('8',lambda : self.Plateau.jouerMouvement(7))
        self.accept('9',lambda : self.Plateau.jouerMouvement(8))
        self.accept('r',self.Plateau.reset)
        self.accept('a',self.Plateau.annulerMouvement)
        self.accept('d',self.Plateau.dechargerGraphismes)
        self.accept('c',self.Plateau.chargerGraphismes)
        self.accept('t',self.test)

    def test(self):
        if self.Plateau.mouvementPossible() != []:
            self.Plateau.jouerMouvement(self.IA.IA.meilleurMouvement())



app = MyApp()
app.run()
