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
from direct.showbase import DirectObject
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TransparencyAttrib

class Menu(DirectObject.DirectObject):
    def __init__(self, loader, chargerGraphismes, dechargerGraphismes, son, reset):
        self.__chargerGraphismes = chargerGraphismes
        self.__dechargerGraphismes = dechargerGraphismes
        self.loader = loader
        self.reset = reset
        self.son = son
        self.chargersfx()
        self.Chargerboutons()
        self.menu()
    def Chargerboutons(self):
        self.b4= DirectButton(text =("Settings"),scale=0.2,text_scale=(0.6,0.6), pos = (-0.95,0,0.80),command=self.dechargerjeupouroptions,clickSound=(self.buttonson))
        self.b3= DirectButton(text = ("Reset", "click!", "Reset", "disabled"), scale=.18, pos = (0.95,0,0.80), command = self.reset,clickSound=self.resetsound)    #def Volume(self):
        self.b = DirectButton(text = ("Jouer", "Jouer", "Jouer", "disabled"),text_scale=(0.1,0.2),pos=(0,0,0.5),command=(self.dechargermenupourmenu2),clickSound=(self.buttonson),rolloverSound=(self.rollsound))

        self.b2 = DirectButton(text = ("Settings","Settings","Settings"),text_scale=(0.1,0.2),pos=(0,0,0),command=self.dechargermenupouroptions,clickSound=(self.buttonson))
        self.b5 = DirectButton(text= ("IA Facile"), text_scale=(0.1,0.2),pos=(0,0,0.75),command=self.dechargermenu2pourgraph,clickSound=(self.buttonson))
        self.b6 = DirectButton(text= ("IA Intermediaire"), text_scale=(0.1,0.2),pos=(0,0,0),command=self.dechargermenu2pourgraph,clickSound=(self.buttonson))
        self.b7 = DirectButton(text= ("IA Difficile"), text_scale=(0.1,0.2),pos=(0,0,-0.75),command=self.dechargermenu2pourgraph,clickSound=(self.buttonson))
        self.b.hide()
        self.b5.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.b6.hide()
        self.b7.hide()
    def chargerGraphismes(self):
        self.__chargerGraphismes()
        self.son.Musiquegame.play()
        self.son.Musiquemenu.stop()
        self.b3.show()
        self.b4.show()

    def dechargerGraphismes(self):
        """Efface tous les tours présente et les pions"""
        self.__dechargerGraphismes()
        self.b3.hide()
        self.b4.hide()
    def menu(self):
        self.b.show()
        self.b2.show()
        self.son.LancerMusiquemenu()
        self.son.Musiquegame.stop()
        self.son.Musiquewin.stop()

    def dechargermenupourmenu2(self):
        self.b.hide()
        self.b2.hide()
        self.menu2()

    def dechargermenupouroptions(self):
        self.b.hide()
        self.b2.hide()
        self.Option()

    def dechargermenu2pourgraph(self):
    	self.b5.hide()
    	self.b6.hide()
    	self.b7.hide()
    	self.chargerGraphismes()
    	self.son.Musiquemenu.stop()

    def dechargerjeupouroptions(self):
        self.dechargerGraphismes()
        self.Option()
        self.son.Musiquegame.stop()
        self.son.LancerMusiquemenu()


    def dechargeroptionspourjeu(self):
        self.dechargeroptions()
        self.chargerGraphismes()
        self.son.Musiquemenu.stop()

    def dechargeroptionspourmenu(self):
        self.dechargeroptions()
        self.menu()

    def dechargeroptions(self):
        self.slider.hide()
        self.labelvolume.hide()
        self.retourjeu.hide()
        self.retourmenu.hide()
        self.disablesfx.hide()

    def showValue(self):
    	print (self.slider['value'])
    	self.son.Actualiserson(self.slider['value'])
    def chargersfx(self):
		self.buttonson=self.loader.loadSfx("218721__bareform__boom-bang.aiff")
		self.rollsound=self.loader.loadSfx("swoosh.flac")
		self.resetsound=self.loader.loadSfx("swoosh.flac")

    def disablefx(self,status):
		if status == True:
			self.buttonson.setVolume(0)
			self.rollsound.setVolume(0)
			self.resetsound.setVolume(0)


		else :
			self.buttonson.setVolume(1)
			self.rollsound.setVolume(1)
			self.resetsound.setVolume(1)



    def Option(self):
        self.slider = DirectSlider(range=(0,1), value=0.5, pageSize=0.5,scale=0.4,pos=(0.65,0,0.75),command=(self.showValue)) #PB 1 FAIRE SORTIR VALEUR DANS OPTION
        self.labelvolume = DirectLabel(text=("Volume"),scale=0.5,pos=(-0.65,0,0.75),text_scale=(0.4,0.6))
        self.retourjeu= DirectButton(text=("Resume"),scale=0.5,pos=(-0.65,0,-0.90),text_scale=(0.4,0.6),command= (self.dechargeroptionspourjeu),clickSound=(self.buttonson))
        self.retourmenu= DirectButton(text=("Menu"),scale=0.5,pos=(0.65,0,-0.90),text_scale=(0.4,0.6),command=(self.dechargeroptionspourmenu),clickSound=(self.buttonson))
        self.disablesfx=DirectCheckButton(text=("Disable Sound Effects"),text_scale=(0.4,0.6),scale=0.3,pos=(0,0,0.15),command=self.disablefx)

    def menu2(self):
    	self.b5.show()
    	self.b6.show()
    	self.b7.show()
