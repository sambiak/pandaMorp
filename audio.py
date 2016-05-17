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
class AudioManager():
	def __init__(self, loader):
		self.loader = loader
		self.Musiquewin = self.loader.loadMusic("GreekDance.mp3")
		self.Musiquegame = self.loader.loadMusic("cannontube.ogg")
		self.Musiquegame.setLoop(True)
		print("éxécuté")
		self.Musiquemenu = self.loader.loadMusic("Welcome.flac")
		self.volumeSon = 1
		self.Musiquemenu.setLoop(True)
		self.Musiquemenu.play()

	def Arretermusiques(self):
		self.Musiquewin.stop()
		self.Musiquegame.stop()
		self.buttonson.stop()
		self.rollsound.stop()
		self.resetsound.stop()

	def LancerMusiquevictoire(self):
		if self.Musiquewin.status() != self.Musiquewin.PLAYING:
			self.Musiquewin.play()
			self.Musiquegame.stop()

	def LancerMusiquemenu(self):
		if self.Musiquemenu.status() != self.Musiquemenu.PLAYING:
			self.Musiquemenu.play()
	def LancerMusiquegame(self):
		if self.Musiquegame.status() != self.Musiquegame.PLAYING:
			self.Musiquegame.play()

	def disableaudio(self):
		self.disableAllAudio()


	def Actualiserson(self,Volume):
		self.Musiquegame.setVolume(Volume)
		self.Musiquewin.setVolume(Volume)
		self.Musiquemenu.setVolume(Volume)
