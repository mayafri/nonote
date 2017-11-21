'''
Copyright ou © ou Copr. Maya Friedrichs, (2015) 

mail@hyakosm.net

Ce logiciel est un programme informatique servant à prendre et organiser
des notes. 

Ce logiciel est régi par la licence CeCILL soumise au droit français et
respectant les principes de diffusion des logiciels libres. Vous pouvez
utiliser, modifier et/ou redistribuer ce programme sous les conditions
de la licence CeCILL telle que diffusée par le CEA, le CNRS et l'INRIA 
sur le site "http://www.cecill.info".

En contrepartie de l'accessibilité au code source et des droits de copie,
de modification et de redistribution accordés par cette licence, il n'est
offert aux utilisateurs qu'une garantie limitée.  Pour les mêmes raisons,
seule une responsabilité restreinte pèse sur l'auteur du programme,  le
titulaire des droits patrimoniaux et les concédants successifs.

A cet égard  l'attention de l'utilisateur est attirée sur les risques
associés au chargement,  à l'utilisation,  à la modification et/ou au
développement et à la reproduction du logiciel par l'utilisateur étant 
donné sa spécificité de logiciel libre, qui peut le rendre complexe à 
manipuler et qui le réserve donc à des développeurs et des professionnels
avertis possédant  des  connaissances  informatiques approfondies.  Les
utilisateurs sont donc invités à charger  et  tester  l'adéquation  du
logiciel à leurs besoins dans des conditions permettant d'assurer la
sécurité de leurs systèmes et ou de leurs données et, plus généralement, 
à l'utiliser et l'exploiter dans les mêmes conditions de sécurité. 

Le fait que vous puissiez accéder à cet en-tête signifie que vous avez 
pris connaissance de la licence CeCILL, et que vous en avez accepté les
termes.
'''

# -*- coding: utf8 -*-

import os, fnmatch
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from utilitaire import *

class ClasseNavInt:
	def __init__(self):
		self.racine = "Notes"
		self.cheminDossier = self.racine
		self.cheminFichier = ""
		self.focusDossiers = self.racine
		self.frame = Frame()
		self.separateur = Frame(self.frame, width=0)

		self.imageFichierOuvert = ImageTk.PhotoImage\
		(Image.open('Icones/Ouvert.png'))
		
		self.i1 = ImageTk.PhotoImage(Image.open('Icones/dossierNouveau.png'))
		self.i2 = ImageTk.PhotoImage(Image.open('Icones/dossierSupprimer.png'))
		self.i3 = ImageTk.PhotoImage(Image.open('Icones/dossierRenommer.png'))
		self.i4 = ImageTk.PhotoImage(Image.open('Icones/dossierDeplacer.png'))
		
		self.frameComD = Frame(self.frame)
		
		self.dosNouv = Button(self.frameComD, overrelief=RAISED, relief=FLAT,
		image=self.i1)
		
		self.dosNouv.pack(side=LEFT)
		
		self.dosSuppr = Button(self.frameComD, overrelief=RAISED, relief=FLAT,
		image=self.i2)
		
		self.dosSuppr.pack(side=LEFT)
		
		self.dosRm = Button(self.frameComD, overrelief=RAISED, relief=FLAT,
		image=self.i3)
		
		self.dosRm.pack(side=LEFT)
		
		self.dosDeplacer = Button(self.frameComD, overrelief=RAISED,
		relief=FLAT, image=self.i4)
		
		self.dosDeplacer.pack(side=LEFT)

		self.i11 = ImageTk.PhotoImage(Image.open('Icones/fichierNouveau.png'))
		self.i12 = ImageTk.PhotoImage(Image.open('Icones/fichierSupprimer.png'))
		self.i13 = ImageTk.PhotoImage(Image.open('Icones/fichierRenommer.png'))
		self.i14 = ImageTk.PhotoImage(Image.open('Icones/fichierDeplacer.png'))
		
		self.frameComF = Frame(self.frame)
		
		self.fichNouv = Button(self.frameComF, overrelief=RAISED, relief=FLAT,
		image=self.i11)
		
		self.fichNouv.pack(side=LEFT)
		
		self.fichSuppr = Button(self.frameComF, overrelief=RAISED, relief=FLAT,
		image=self.i12)
		
		self.fichSuppr.pack(side=LEFT)
		
		self.fichRm = Button(self.frameComF, overrelief=RAISED, relief=FLAT,
		image=self.i13)
		
		self.fichRm.pack(side=LEFT)
		
		self.fichDeplacer = Button(self.frameComF, overrelief=RAISED,
		relief=FLAT, image=self.i14)
		
		self.fichDeplacer.pack(side=LEFT)
	
		self.scrollFich = ttk.Scrollbar(self.frame)
		
		self.listeFichiers = ttk.Treeview(self.frame,
		yscrollcommand=self.scrollFich.set, selectmode="browse", show="tree")
		
		self.listeFichiers.column("#0", stretch=NO)
		self.scrollFich.config(command=self.listeFichiers.yview)

		self.scrollDos = ttk.Scrollbar(self.frame)
		
		self.arbreDossiers = ttk.Treeview(self.frame,
		yscrollcommand=self.scrollDos.set, selectmode="browse", show="tree")
		
		self.arbreDossiers.column("#0", stretch=NO)
		self.scrollDos.config(command=self.arbreDossiers.yview)

		self.frameComD.grid(row=0, column=0, columnspan=2)
		self.scrollDos.grid(row=1, column=0, sticky=NSEW)
		self.arbreDossiers.grid(row=1,column=1, sticky=NSEW)
		self.frameComF.grid(row=2, column=0, columnspan=2)
		self.scrollFich.grid(row=3, column=0, sticky=NSEW)
		self.listeFichiers.grid(row=3,column=1, sticky=NSEW)
		
		ttk.Separator(self.frame,orient=VERTICAL).grid(row=0,
		column=2, rowspan=4, sticky=NSEW)

		self.frame.rowconfigure(1,weight=1)
		self.frame.rowconfigure(3,weight=1)

		self.AfficherDossiers()
		self.AfficherFichiers()

	def AfficherDossiers(self, toto=0):
		if self.arbreDossiers.exists(self.racine) == True:
			self.arbreDossiers.delete(self.racine)

		self.arbreDossiers.insert("", 0, self.racine, text=self.racine)
		self.arbreDossiers.item(self.racine, open=True)
		self.arbreDossiers.selection_set(self.racine)
		self.arbreDossiers.focus(self.racine)

		for root, dirs, files in os.walk(self.racine):     
			i = 0
			while i < len(dirs):
  				self.arbreDossiers.insert(root, i, root+s()+dirs[i],
  				text=dirs[i])
  				i = i+1
		
		def SetFocusDossiers(void=0):
			self.focusDossiers = self.arbreDossiers.focus()
			self.cheminDossier = self.focusDossiers
			self.AfficherFichiers()
			
		self.arbreDossiers.bind("<<TreeviewSelect>>", SetFocusDossiers)

	def AfficherFichiers(self):
		def SetFocusFichiers(void=0):
			self.focusFichiers = self.listeFichiers.focus()

		self.focusFichiers = ""

		for element in self.listeFichiers.get_children():
			self.listeFichiers.delete(element)

		fichiersFiltres = fnmatch.filter(os.listdir(self.focusDossiers),
		"*.nonote")
		
		for i in fichiersFiltres:
			self.listeFichiers.insert("", 0, self.focusDossiers+s()+i,
			text=i.replace('.nonote',''))

		if self.cheminFichier != "":
			try:
				self.listeFichiers.item(self.cheminFichier,
				image=self.imageFichierOuvert)
			except:
				pass

		self.listeFichiers.bind("<<TreeviewSelect>>", SetFocusFichiers)

