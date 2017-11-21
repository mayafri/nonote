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

from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
from decodeur import *
import platform
from PIL import ImageTk
from PIL import Image

def Guide(self):
			
	# MENU PRINCIPAL
	def Accueil():
		# Suppression FenConf de la rubrique (si ouverte)
		cadre.grid_remove()
		boutonFermerRub.grid_remove()
	
		# Affichage menu
		label.grid(row=0, column=0, padx=5, pady=5)
		bouton1.grid(row=1, column=0, padx=5, pady=5, sticky='EW')
		bouton2.grid(row=2, column=0, padx=5, pady=5, sticky='EW')
		bouton3.grid(row=3, column=0, padx=5, pady=5, sticky='EW')
		bouton4.grid(row=4, column=0, padx=5, pady=5, sticky='EW')
		bouton5.grid(row=5, column=0, padx=5, pady=5, sticky='EW')
		boutonFermer.grid(row=6, column=0, padx=5, pady=5)

	# MODÈLE DE RUBRIQUE
	def Afficher(type):
		# Suppression FenConf du menu
		label.grid_remove()
		bouton1.grid_remove()
		bouton2.grid_remove()
		bouton3.grid_remove()
		bouton4.grid_remove()
		bouton5.grid_remove()
		boutonFermer.grid_remove()
	
		# Ouverture fichier texte de la rubrique
		fichier = open("Guide/"+type+".nonote", 'r', encoding='utf-8')
		varFichier = fichier.read()
		fichier.close()
	
		# Configuration du widget de texte
		cadre.delete("0.0", END)
		
		### Décodage

		balises = ['GRAS', 'JAUNE', 'T1', 'AVERTISSEMENT', 'CODE']
		cadre.insert(END, FichSupprBalises(balises, varFichier))

		for i in balises:
			p1 = FichChPositions(balises, varFichier, i)
			p2 = FichChPositions(balises, varFichier, "/"+i)
			ii = 0
			while ii < len(p2):
				cadre.tag_add(i, p1[ii], p2[ii])
				ii += 1
				
		### Insertion des images

		self.imagesGuide = []
		listeUrlImage = FichChercherImages(varFichier)
		
		if len(listeUrlImage) > 0:	
			for i in listeUrlImage:
				try:
					self.imagesGuide.append(ImageTk.PhotoImage\
					(Image.open("Guide/Images/"+i), name=i))
				except:
					pass
			
			listePositionsImage = FichChPositionsImages(varFichier)
		
			i = 0
			while i < len(self.imagesGuide):
				cadre.image_create(listePositionsImage[i],
				image=self.imagesGuide[i])
				i += 1

		police = font.Font(family='Times', size=10)
		cadre.config(highlightthickness=0, wrap='word', width=35, height=15,
		font=police)
		
		# Affichage de la rubrique
		cadre.grid(row=0, column=0)
		boutonFermerRub.grid(row=1, column=0)

	# TYPES DE RUBRIQUES
	def Presentation():
		Afficher("presentation")

	def Tuto():
		Afficher("tuto")

	def Classer():
		Afficher("classer")

	def Avance():
		Afficher("avance")

	def Technique():
		Afficher("technique")

	# FENÊTRE
	Fenetre = Toplevel()

	# Propriétés de la fenêtre
	if platform.system() == "Windows":
		Fenetre.iconbitmap('Icones\logo.ico')

	Fenetre.title("Guide")
	Fenetre.resizable(False,False)
	
	# Widgets du menu
	label = Label(Fenetre, text="\
Bienvenue dans le guide, vous pouvez\n\
garder cette fenêtre ouverte tout en\n\
utilisant Nonote.")

	bouton1 = ttk.Button(Fenetre, text="Présentation du logiciel",
	command=Presentation)
	bouton2 = ttk.Button(Fenetre, text="Ma première note",
	command=Tuto)
	bouton3 = ttk.Button(Fenetre, text="Gérer et Classer ses notes",
	command=Classer)
	bouton4 = ttk.Button(Fenetre, text="Fonctions avancées",
	command=Avance)
	bouton5 = ttk.Button(Fenetre, text="Informations Techniques",
	command=Technique)
	boutonFermer = ttk.Button(Fenetre, text="Fermer",
	command=Fenetre.destroy)

	# Widgets pour les rubriques
	cadre = ScrolledText(Fenetre)

	PoliceGras = font.Font(family='Times', weight='bold', size=10)
	PoliceT1 = font.Font(family='Times', size=16, weight='bold')
	PoliceCode = font.Font(family="Liberation Mono", size=10)

	cadre.tag_configure("GRAS", font=PoliceGras)
	cadre.tag_configure("CODE", font=PoliceCode)
	cadre.tag_configure("JAUNE", background="#FFFF00")	
	cadre.tag_configure("T1", font=PoliceT1)	
	
	boutonFermerRub = ttk.Button(Fenetre, text="Fermer", command=Accueil)

	# Envoi du menu
	Accueil()
	
	Fenetre.mainloop()

