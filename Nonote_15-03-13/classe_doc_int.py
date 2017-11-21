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

import os, tkinter.font
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
from PIL import Image, ImageTk

from utilitaire import *

class ClasseDocInt:
	def __init__(self, texte_police, texte_taille, couleur_fond, largeur_texte,
	taille_tab):
		self.frame = Frame()
		self.frameDoc = Frame(self.frame)
		self.scroll = ttk.Scrollbar(self.frame)
		self.Doc = Text(self.frameDoc, yscrollcommand=self.scroll.set)
		self.scroll.config(command=self.Doc.yview)
		
		self.Doc.tag_configure(SEL, background="#000000", foreground="#FFFFFF")

		self.TexteTailleDefaut = texte_taille
		self.TextePolice = texte_police
		self.TexteTaille = self.TexteTailleDefaut
		self.Police = font.Font(family=self.TextePolice, size=self.TexteTaille)
		
		self.PoliceGras = font.Font(family=self.TextePolice,
		size=self.TexteTaille, weight='bold')
		
		self.PoliceT1 = font.Font(family=self.TextePolice,
		size=int(self.TexteTaille*2.5))
		
		self.PoliceT2 = font.Font(family=self.TextePolice,
		size=int(self.TexteTaille*2))
		
		self.PoliceT3 = font.Font(family=self.TextePolice,
		size=int(self.TexteTaille*1.6))
		
		self.PoliceT4 = font.Font(family=self.TextePolice,
		size=int(self.TexteTaille*1.3))
		
		self.PoliceCite = font.Font(family=self.TextePolice,
		size=self.TexteTaille, slant="italic")
		
		self.PoliceAuteur = font.Font(family=self.TextePolice,
		size=int(self.TexteTaille/1.5))
		
		self.Doc.config(highlightthickness=0, font=self.Police, wrap='word',
		width=largeur_texte, height=500, relief='flat', borderwidth=0)
		
		self.CouleurFond(couleur_fond)
		
		self.PoliceCode = font.Font(family="Liberation Mono",
		size=self.TexteTaille-1)
			
		self.i1 = ImageTk.PhotoImage(Image.open('Icones/EnrFichier.png'))
		self.i2 = ImageTk.PhotoImage(Image.open('Icones/EnrFichierRouge.png'))
		self.i3 = ImageTk.PhotoImage(Image.open('Icones/Undo.png'))
		self.i4 = ImageTk.PhotoImage(Image.open('Icones/Redo.png'))
		self.i9 = ImageTk.PhotoImage(Image.open('Icones/Gras.png'))
		self.i10 = ImageTk.PhotoImage(Image.open('Icones/SurlignJaune.png'))
		self.i12 = ImageTk.PhotoImage(Image.open('Icones/SurlignBleu.png'))
		self.i11 = ImageTk.PhotoImage(Image.open('Icones/SurlignVert.png'))
		self.i13 = ImageTk.PhotoImage(Image.open('Icones/SurlignRien.png'))
		self.i14 = ImageTk.PhotoImage(Image.open('Icones/Code.png'))
		self.i15 = ImageTk.PhotoImage(Image.open('Icones/image.png'))
		self.i16 = ImageTk.PhotoImage(Image.open('Icones/imageweb.png'))
		self.i17 = ImageTk.PhotoImage(Image.open('Icones/imagecreer.png'))
		self.i18 = ImageTk.PhotoImage(Image.open('Icones/efForm.png'))

		self.mi = ImageTk.PhotoImage(Image.open('Icones/Bienvenue.png'))
		self.mi2 = ImageTk.PhotoImage(Image.open('Icones/BienvenuePlus.png'))
		
		def ea():
			self.messageImage.configure(image=self.mi2, command=ea2)
		def ea2():
			self.messageImage.configure(image=self.mi, command=ea)

		self.message = Frame(self.frame)
		self.mi = ImageTk.PhotoImage(Image.open('Icones/Bienvenue.png'))
		
		self.messageLabel = Label(self.message, text=
		"Bienvenue, créez ou ouvrez un document pour commencer.")
		
		self.messageImage = Button(self.message, relief=FLAT, image=self.mi,
		command=ea)
		
		self.messageImage.pack(side=LEFT)
		self.messageLabel.pack(side=LEFT)
		
		self.barreOutils = Frame(self.frame)

		self.boutonEnr = Button(self.barreOutils, overrelief=RAISED,
		relief=FLAT, image=self.i1)
		
		self.boutonEnr.pack(side=LEFT)

		ttk.Separator(self.barreOutils,orient=VERTICAL).pack(side=LEFT,
		fill=BOTH)

		self.boutonUndo = Button(self.barreOutils, overrelief=RAISED,
		relief=FLAT, image=self.i3, state=DISABLED)
		
		self.boutonRedo = Button(self.barreOutils, overrelief=RAISED,
		relief=FLAT, image=self.i4, state=DISABLED)
		
		self.boutonUndo.pack(side=LEFT)
		self.boutonRedo.pack(side=LEFT)

		ttk.Separator(self.barreOutils,orient=VERTICAL).pack(side=LEFT,
		fill=BOTH)

		self.boutonGras = Button(self.barreOutils, overrelief=RAISED,
		relief=FLAT, image=self.i9)
		
		self.boutonGras.pack(side=LEFT)
		self.boutonCode = Button(self.barreOutils, overrelief=RAISED,
		relief=FLAT, image=self.i14)
		
		self.boutonCode.pack(side=LEFT)
		
		typeParagraphe = ["Paragraphe", "Titre 1", "Titre 2", "Titre 3",
		"Titre 4", "Citation", "Source", "Avertissement", "Conseil"]
		
		self.choixTypePar = ttk.Combobox(self.barreOutils,
		values=typeParagraphe, state='readonly')
		
		self.choixTypePar.pack(side=LEFT)

		self.boutonSurlignRien = Button(self.barreOutils, overrelief=RAISED,
		relief=FLAT, image=self.i13)
		
		self.boutonSurlignRien.pack(side=LEFT)

		self.boutonSurlignJaune = Button(self.barreOutils, overrelief=RAISED,
		relief=FLAT, image=self.i10)
		
		self.boutonSurlignJaune.pack(side=LEFT)

		self.boutonSurlignVert = Button(self.barreOutils, overrelief=RAISED,
		relief=FLAT, image=self.i11)
		
		self.boutonSurlignVert.pack(side=LEFT)

		self.boutonSurlignBleu = Button(self.barreOutils, overrelief=RAISED,
		relief=FLAT, image=self.i12)
		
		self.boutonSurlignBleu.pack(side=LEFT)
		
		ttk.Separator(self.barreOutils,orient=VERTICAL).pack(side=LEFT,
		fill=BOTH)
		
		self.efForm = Button(self.barreOutils, overrelief=RAISED, relief=FLAT,
		image=self.i18)
	
		self.efForm.pack(side=LEFT)

		ttk.Separator(self.barreOutils,orient=VERTICAL).pack(side=LEFT,
		fill=BOTH)
		
		self.boutonImage = Button(self.barreOutils, overrelief=RAISED,
		relief=FLAT, image=self.i15)
		
		self.boutonImage.pack(side=LEFT)
		
		self.boutonImageWeb = Button(self.barreOutils, overrelief=RAISED,
		relief=FLAT, image=self.i16)
		
		self.boutonImageWeb.pack(side=LEFT)
		
		self.boutonCreerDessin = Button(self.barreOutils, overrelief=RAISED,
		relief=FLAT, image=self.i17)
		
		self.boutonCreerDessin.pack(side=LEFT)
		
		ttk.Separator(self.barreOutils,orient=VERTICAL).pack(side=LEFT,
		fill=BOTH)

		self.barreOutils.grid(row=0, column=0, columnspan=2, sticky=NSEW)
		
		ttk.Separator(self.frame,orient=HORIZONTAL).grid(row=1, column=0,
		columnspan=2, sticky=NSEW)
		
		self.BarreEtat()
		
		self.frameDoc.grid(row=2, column=0, sticky=NSEW)
		self.Doc.pack(side=LEFT, padx=20)
		self.scroll.grid(row=2, column=1, sticky=NSEW)
		self.frameEtat.grid(row=3, column=1, sticky=EW)

		self.frame.rowconfigure(2,weight=1)
		self.frame.columnconfigure(0,weight=1)

	def BarreEtat(self):
		self.frameEtat = Frame()
		
		self.nbLignesIdent = Label(self.frameEtat, text="Lignes :")
		self.nbMotsIdent = Label(self.frameEtat, text="Mots :")
		self.posIdent = Label(self.frameEtat, text="Position :")
		
		self.nbLignes = Label(self.frameEtat, text="0")
		self.nbMots = Label(self.frameEtat, text="0")
		self.pos = Label(self.frameEtat, text="0.0")

		self.etatSauv = Label(self.frameEtat, text="Enregistré")
		
		ttk.Separator(self.frameEtat).pack(fill=BOTH)
		self.nbLignesIdent.pack(side=LEFT)
		self.nbLignes.pack(side=LEFT)
		ttk.Separator(self.frameEtat,orient=VERTICAL).pack(side=LEFT, fill=BOTH,
		padx=5)
		self.nbMotsIdent.pack(side=LEFT)
		self.nbMots.pack(side=LEFT)
		ttk.Separator(self.frameEtat,orient=VERTICAL).pack(side=LEFT, fill=BOTH,
		padx=5)
		self.posIdent.pack(side=LEFT)
		self.pos.pack(side=LEFT)
		ttk.Separator(self.frameEtat,orient=VERTICAL).pack(side=LEFT, fill=BOTH,
		padx=5)
		self.etatSauv.pack(side=LEFT)

	def CouleurFond(self, couleur):
		if couleur == "Blanc":
			self.Doc.config(bg='#FFFFFF')
			self.frameDoc.config(bg='#FFFFFF')
		if couleur == "Gris":
			self.Doc.config(bg='#e0e0e0')
			self.frameDoc.config(bg='#e0e0e0')
		if couleur == "Jaune":
			self.Doc.config(bg='#ffffcb')
			self.frameDoc.config(bg='#ffffcb')
		if couleur == "Vert":
			self.Doc.config(bg='#eeffcb')
			self.frameDoc.config(bg='#eeffcb')
		if couleur == "Bleu":
			self.Doc.config(bg='#e6f6ff')
			self.frameDoc.config(bg='#e6f6ff')
		if couleur == "Mauve":
			self.Doc.config(bg='#eee0f9')
			self.frameDoc.config(bg='#eee0f9')

