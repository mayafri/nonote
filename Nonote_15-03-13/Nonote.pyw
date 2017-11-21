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

import os, platform, shutil, tkinter, re, webbrowser, time
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
from PIL import ImageTk
from PIL import Image as ImagePIL

from classe_nav import *
from classe_doc import *
from utilitaire import *
from decodeur import *
from menus import *
from menus_mini import *
from raccourcis import *
from themelinux import *

os.chdir(os.path.dirname(__file__))

class Nonote:
	def __init__(self):
		# Variables par défaut du fichier de configuration

		self.ChargerConf()

		# Définition de la fenêtre, de ses propriétés et de son contenu

		self.fenetre = Tk()
		self.titre_fenetre = "Nonote"
		self.fenetre.title(self.titre_fenetre)
		self.fenetre.geometry(self.geometrie)
		
		# Routines de début de chargement
		
		EcranChargement(self)
		try:
		 os.mkdir("Temporaire")
		 os.mkdir("Temporaire/AnnulerRefaire")
		except:
			pass

		if platform.system() == "Windows":
			self.fenetre.iconbitmap('Icones\\logo.ico')

		# Création des objets, disposition de la fenêtre

		self.ObjNav = ClasseNav()
		self.ObjDoc = ClasseDoc(self.texte_police,
		int(self.texte_taille), self.couleur_fond, int(self.largeur_texte), 4)

		self.SepaGlobal = ttk.Separator(self.fenetre,orient=HORIZONTAL)
		self.SepaGlobal.grid(row=1, column=1, sticky=NSEW)

		self.ObjNav.frame.grid(row=0, column=0, rowspan=4, sticky=NSEW)
		self.ObjDoc.frame.grid(row=2, column=1, sticky=NSEW)

		self.fenetre.rowconfigure(2,weight=1)
		self.fenetre.columnconfigure(1,weight=1)
		
		# Gestion du style spécifique à Linux
		
		ThemeLinux(self)

		# Balises de mise en forme du texte

		self.balises = ['GRAS', 'JAUNE', 'VERT', 'BLEU', 'T1', 'T2', 'T3', 'T4',
		'CITATION', 'AVERTISSEMENT', 'CONSEIL', 'AUTEUR', 'CODE']
		self.ObjDoc.balises = self.balises

		# Relais pour les commandes générales

		self.ObjNav.listeFichiers.bind("<Double-Button-1>", self.DocOuvrir)
		self.fenetre.protocol("WM_DELETE_WINDOW", self.ActionFermer)

		self.ObjDoc.boutonUndo.configure(command=self.Undo)
		self.ObjDoc.boutonRedo.configure(command=self.Redo)
		
		# Ressources
		
		self.bandeau = ""
		self.imagesGuide = []
		self.imageFausse = PhotoImage()

		self.imageFichierOuvert =\
		ImageTk.PhotoImage(ImagePIL.open('Icones/Ouvert.png'))

		# Gestion du plein écran

		self.f_full_check = IntVar()

		if self.f_full == 1:
			self.fenetre.attributes('-fullscreen', 1)
			self.f_full_check.set(1)

		# Chargement de l'écran d'Accueil

		self.DocOuvrir(fermer=True)

		# Affichage

		BarreMenusMini(self)
		FermerChargement(self)
		self.fenetre.mainloop()
		
		# Routines de fin

		shutil.rmtree("Temporaire")

	def Undo(self, toto=0):
		self.ObjDoc.SauvFuturUndoRedo(self)
		self.ObjDoc.Doc.delete(0.0, END)
		self.ObjDoc.indexAR -= 1
		self.Ouverture("Temporaire/AnnulerRefaire/"+str(self.ObjDoc.indexAR))
		
		self.ObjDoc.Doc.mark_set(INSERT, self.ObjDoc.indexPosAR[self.ObjDoc.indexAR])
		self.ObjDoc.Doc.see(INSERT)
		self.ObjDoc.Traqueur()

	def Redo(self, toto=0):
		self.ObjDoc.Doc.delete(0.0, END)
		self.ObjDoc.indexAR += 1
		self.Ouverture("Temporaire/AnnulerRefaire/"+str(self.ObjDoc.indexAR))

		self.ObjDoc.Doc.mark_set(INSERT, self.ObjDoc.indexPosAR[self.ObjDoc.indexAR])
		self.ObjDoc.Doc.see(INSERT)
		self.ObjDoc.Traqueur()


	def ChargerConf(self):
		# Chargement du fichier de configuration

		conf = open("Special/config.txt", 'r', encoding='utf-8')

		conf_str = conf.read()
		conf_str = re.sub('\n*', '', conf_str)

		geometrie = re.sub('.*<GEOMETRIE>', '', conf_str)
		self.geometrie = re.sub('</GEOMETRIE>.*', '', geometrie)
		f_full = re.sub('.*<F_FULL>', '', conf_str)
		f_full = re.sub('</F_FULL>.*', '', f_full)
		try:
			self.f_full = int(f_full)
		except:
			self.f_full = ""
		texte_taille = re.sub('.*<TEXTE_TAILLE>', '', conf_str)
		self.texte_taille = re.sub('</TEXTE_TAILLE>.*', '', texte_taille)
		texte_police = re.sub('.*<TEXTE_POLICE>', '', conf_str)
		self.texte_police = re.sub('</TEXTE_POLICE>.*', '', texte_police)
		couleur_fond = re.sub('.*<COULEUR_FOND>', '', conf_str)
		self.couleur_fond = re.sub('</COULEUR_FOND>.*', '', couleur_fond)
		largeur_texte = re.sub('.*<LARGEUR_TEXTE>', '', conf_str)
		self.largeur_texte = re.sub('</LARGEUR_TEXTE>.*', '', largeur_texte)
		
		self.texte_taille = int(self.texte_taille)
		
		conf.close()

	# Décodage d'un fichier et insertion dans la zone de texte

	def Ouverture(self, cheminFichier, toto=0):
		self.ObjDoc.Doc.delete(0.0, END)

		fichier_brut = open(cheminFichier, 'r', encoding='utf-8')
		fichier = str(fichier_brut.read())

		# Décodage

		self.ObjDoc.Doc.insert(END, FichSupprBalises(self.balises, fichier))

		for i in self.balises:
			p1 = FichChPositions(self.balises, fichier, i)
			p2 = FichChPositions(self.balises, fichier, "/"+i)
			ii = 0
			while ii < len(p2):
				self.ObjDoc.Doc.tag_add(i, p1[ii], p2[ii])
				ii += 1
				
		# Insertion des images
				
		self.ObjDoc.image = []
		listeUrlImage = FichChercherImages(fichier)
		
		if len(listeUrlImage) > 0:	
			for i in listeUrlImage:
				try:
					self.ObjDoc.image.append(ImageTk.PhotoImage\
					(ImagePIL.open("./Images/"+i), name=i))
				except:
					self.ObjDoc.image.append(ImageTk.PhotoImage\
					(ImagePIL.open("./Icones/erreurImage.png"), name=i))
			
			listePositionsImage = FichChPositionsImages(fichier)
		
			i = 0
			while i < len(self.ObjDoc.image):
				self.ObjDoc.Doc.image_create(listePositionsImage[i],
				image=self.ObjDoc.image[i])
				i += 1
				
		# Génération des liens
		# (la génération des autres balises se fait automatiquement)
		self.ObjDoc.GenLiens()
		
		fichier_brut.close()
		self.ObjDoc.InfosBarreEtat(ouverture=True)

	# Commandes pour ouvrir ou fermer un document

	def DocOuvrir(self, position=0, fermer=False):
		if fermer == False:
			cheminFichier =\
			self.ObjNav.listeFichiers.identify_row(position.y)
			
			self.ObjDoc.indexAR = 0
			shutil.rmtree("Temporaire/AnnulerRefaire")
			os.mkdir("Temporaire/AnnulerRefaire")
			shutil.copy(cheminFichier, "Temporaire/AnnulerRefaire/0")
			
			barreMenus(self)

			self.ObjDoc.Doc.config(state='normal',undo=1)
		
			self.ObjDoc.barreOutils.grid(row=0, column=0, columnspan=2,
			sticky=NSEW)
		
			self.ObjDoc.message.grid_forget()
			
			RaccourcisFormatage(self)
		else:
			cheminFichier = "Special/bienvenue.nonote"
			BarreMenusMini(self)
			RaccourcisFormatage(self, fermer=True)

		def FlecheEff():
			try:
				self.ObjNav.listeFichiers.item(self.ObjDoc.cheminFichier,
				image=self.imageFausse)
			except:
				pass
				
		self.ObjDoc.Traqueur()
		
		def EnrVerif():
			fichierCode = Codeur(self.balises, self.ObjDoc.Doc.dump(0.0, END),
			self.ObjDoc.image)

			if fichierCode != self.ObjDoc.fichierVerif:
				question = messagebox.askyesnocancel(
				message="Voulez-vous enregistrer vos modifications avant de \
quitter ?",	icon='question', title="Vous ouvrez un autre document") 

				if question == True:
					self.ObjDoc.Enr(self.ObjDoc)
					FlecheEff()
					ImgSupprInutile(self.ObjDoc.image, fichierCode)
					
					self.Ouverture(cheminFichier)
				elif question == False:
					FlecheEff()
					
					fichier_brut = open(self.ObjDoc.cheminFichier, 'r',
					encoding='utf-8')
					
					ImgSupprInutile(self.ObjDoc.image, str(fichier_brut.read()))
					fichier_brut.close()
					
					self.Ouverture(cheminFichier)
					
			else:
				ImgSupprInutile(self.ObjDoc.image, fichierCode)
				FlecheEff()
				self.Ouverture(cheminFichier)

		if fermer == False:			
			if self.ObjNav.listeFichiers.identify_row(position.y) != "":
				if self.ObjDoc.cheminFichier != "" :
					EnrVerif()		
				else:
					self.Ouverture(cheminFichier)
					
			self.fenetre.title("Nonote : "+CheminBeau(cheminFichier))
			self.ObjDoc.cheminFichier = cheminFichier
			self.ObjNav.cheminFichier = cheminFichier
			self.ObjDoc.Doc.edit_reset() 
		
			self.ObjDoc.fichierVerif = Codeur(self.balises,
			self.ObjDoc.Doc.dump(0.0, END), self.ObjDoc.image)
		
			self.ObjNav.listeFichiers.item(cheminFichier,
			image=self.imageFichierOuvert)
		else:
			self.ObjDoc.message.grid(row=0, column=0, columnspan=2,
			sticky=NSEW)

			if self.ObjDoc.cheminFichier != "" :
				EnrVerif()
			else:
				self.Ouverture(cheminFichier)

			self.ObjDoc.Doc.config(state='disabled')
			self.ObjDoc.cheminFichier = ""
			self.ObjNav.cheminFichier = ""
			self.fenetre.title(self.titre_fenetre)
			self.ObjDoc.barreOutils.grid_forget()

	# Fermeture de l'application

	def ActionFermer(self, toto=0):
		def TailleFen():
			x = str(self.fenetre.winfo_width())
			y = str(self.fenetre.winfo_height())
			conf = open("Special/config.txt", 'r', encoding='utf-8')
			conf_str = conf.read()
			conf = open("Special/config.txt", 'w', encoding='utf-8')
			
			if self.f_full == 0:
				conf_str = re.sub('<GEOMETRIE>.*</GEOMETRIE>',
				'<GEOMETRIE>'+x+'x'+y+'</GEOMETRIE>', conf_str)
				
			conf_str = re.sub('<F_FULL>.*</F_FULL>',
			'<F_FULL>'+str(self.f_full)+'</F_FULL>', conf_str)
			
			conf.write(conf_str)
			conf.close()
		
		if self.ObjDoc.cheminFichier != "" :
			fichierCode = Codeur(self.balises, self.ObjDoc.Doc.dump(0.0, END),
			self.ObjDoc.image)
		
			if fichierCode != self.ObjDoc.fichierVerif:			
				question = messagebox.askyesnocancel(
				message="Voulez-vous enregistrer vos modifications avant de \
quitter ?",	icon='question', title="Vous quittez Nonote") 

				if question == True:
					self.ObjDoc.Enr(self.ObjDoc)
					TailleFen()
					self.fenetre.destroy()
					
					ImgSupprInutile(self.ObjDoc.image, fichierCode)
					
				elif question == False:
					TailleFen()
					self.fenetre.destroy()
					
					fichier_brut = open(self.ObjDoc.cheminFichier, 'r',
					encoding='utf-8')
					
					ImgSupprInutile(self.ObjDoc.image, str(fichier_brut.read()))
					fichier_brut.close()
					
				else: # Ça, c'est à cause d'un bug de Mac OS X
					self.fenetre.mainloop()
			else:
				ImgSupprInutile(self.ObjDoc.image, fichierCode)
				TailleFen()
				self.fenetre.destroy()
		else:
			TailleFen()
			self.fenetre.destroy()

Application = Nonote()
