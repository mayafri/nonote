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

import os, platform, shutil, time, re, webbrowser, urllib.request
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from codeur import *
from utilitaire import *

from classe_doc_int import *

class ClasseDoc(ClasseDocInt):
	def __init__(self, texte_police, texte_taille, couleur_fond, largeur_texte,
	taille_tab):
		ClasseDocInt.__init__(self, texte_police, texte_taille, couleur_fond,
		largeur_texte, taille_tab)

		self.fichierVerif = ""
		self.cheminFichier = ""
		self.image = []
		
		self.indexAR = 0
		self.indexMaxAR = 0
		self.indexPosAR = []

		self.boutonEnr.configure(command=self.Enr)

		self.Gras_check = IntVar()
		self.boutonGras.configure(command=self.Gras)
		self.Doc.tag_configure("GRAS", font=self.PoliceGras)
		
		self.Code_check = IntVar()
		self.boutonCode.configure(command=self.Code)
		self.Doc.tag_configure("CODE", font=self.PoliceCode)
		self.tailleTab = taille_tab
		self.Doc.bind("<Tab>", self.Tab)
		self.Doc.bind("<BackSpace>", self.Effacement)
		
		self.Surligner_check = IntVar()
		self.boutonSurlignRien.configure(command=self.SurlignRien)
		self.boutonSurlignJaune.configure(command=self.SurlignJaune)
		self.Doc.tag_configure("JAUNE", background="#FFFF00")
		self.boutonSurlignVert.configure(command=self.SurlignVert)
		self.Doc.tag_configure("VERT", background="#00FF00")
		self.boutonSurlignBleu.configure(command=self.SurlignBleu)
		self.Doc.tag_configure("BLEU", background="#00FFFF")
		
		self.efForm.configure(command=self.SupprFormatage)
		
		self.Styles_check = IntVar()
		self.choixTypePar.bind("<<ComboboxSelected>>", self.TypePar)
		self.Doc.tag_configure("T1", font=self.PoliceT1)
		self.Doc.tag_configure("T2", font=self.PoliceT2)
		self.Doc.tag_configure("T3", font=self.PoliceT3)
		self.Doc.tag_configure("T4", font=self.PoliceT4)
		self.Doc.tag_configure("CITATION",
		font=self.PoliceCite, lmargin1="20", lmargin2="20")
		self.Doc.tag_configure("AVERTISSEMENT", foreground="#ea0000",
		lmargin1="20", lmargin2="20", font=self.PoliceGras)
		self.Doc.tag_configure("CONSEIL", foreground="#007f7f",
		lmargin1="20", lmargin2="20", font=self.PoliceGras)
		self.Doc.tag_configure("AUTEUR", font=self.PoliceAuteur,
		lmargin1="80", lmargin2="80")
		
		self.Doc.tag_configure("LIEN", foreground="blue", underline=1)

		self.Doc.tag_raise(SEL)
		
		self.Doc.tag_bind("LIEN", "<Enter>", self.EntrerLien)
		self.Doc.tag_bind("LIEN", "<Leave>", self.SortirLien)
		self.Doc.tag_bind("LIEN", "<Button-1>", self.Lien)
			
		self.boutonImage.configure(command=self.Image)
		self.boutonImageWeb.configure(command=self.ImageWeb)
		self.boutonCreerDessin.configure(command=self.CreerDessin)
		
		self.Doc.bind("<KeyPress>", self.InfosBarreEtat)
		self.Doc.bind("<ButtonRelease>", self.InfosBarreEtat)
		
		self.Doc.bind("<KeyRelease>", self.Traqueur)
		self.Doc.bind("<ButtonRelease>", self.Traqueur, add="+")	
		
		self.Doc.bind("<space>", self.SauvUndoRedo)
		self.Doc.bind("<KeyRelease-space>", self.GenLiens)
		self.Doc.bind("<Return>", self.Entree)
		
		self.Doc.bind("<Button-1>", self.EffacerMenu)
		if platform.system() == "Darwin":
			self.Doc.bind("<Button-2>", self.MenuContextuel)
		else:
			self.Doc.bind("<Button-3>", self.MenuContextuel)

		self.balises = []

	def Tab(self, toto=0):
		self.Doc.insert("insert", " "*self.tailleTab)
		return("break")
		
	def Effacement(self, toto=0):
		finDeTab = "insert -"+str(self.tailleTab)+"c"
		if self.Doc.get(finDeTab, "insert") == " "*self.tailleTab:
			self.Doc.delete(finDeTab, "insert")
			return("break")

	def DeplDroite(self, toto=0):
		self.DeplElem(dir='droite')
		
	def DeplGauche(self, toto=0):
		self.DeplElem(dir='gauche')

	def DeplElem(self, dir):
		sel1 = self.Doc.index(SEL_FIRST)
		sel2 =  self.Doc.index(SEL_LAST)
		selec = self.Doc.get(SEL_FIRST, SEL_LAST)
		self.Doc.delete(SEL_FIRST,SEL_LAST)
		
		if dir == "droite":
			self.Doc.insert(INSERT+'+1c', selec)
			self.Doc.tag_add("sel", sel1+'+1c', sel2+'+1c')
			self.Doc.mark_set(INSERT, INSERT+'+1c')
		if dir == "gauche":
			self.Doc.insert(INSERT+'-1c', selec)
			self.Doc.tag_add("sel", sel1+'-1c', sel2+'-1c')
			self.Doc.mark_set(INSERT, INSERT+'-1c')

	def EntrerLien(self, toto):
		self.Doc.config(cursor="hand2")
	def SortirLien(self, toto):
		self.Doc.config(cursor="xterm")
	def Lien(self, toto):
		protocoles = ["http://", "https://", "ftp://", "sftp://"]
		for protocole in protocoles:
			debutLien = self.Doc.search(protocole, CURRENT, backwards=True)
			finLien = self.Doc.search(" ", CURRENT)
			webbrowser.open(self.Doc.get(debutLien, finLien))
		
	def Entree(self, toto):
		self.Doc.insert("insert", "\n")
		try:
			self.Doc.tag_remove("T1", "insert linestart",
			"insert linestart + 1 lines")
			self.Doc.tag_remove("T2", "insert linestart",
			"insert linestart + 1 lines")
			self.Doc.tag_remove("T3", "insert linestart",
			"insert linestart + 1 lines")
			self.Doc.tag_remove("T4", "insert linestart",
			"insert linestart + 1 lines")
			self.Doc.tag_remove("CITATION", "insert linestart",
			"insert linestart + 1 lines")
			self.Doc.tag_remove("AVERTISSEMENT", "insert linestart",
			"insert linestart + 1 lines")
			self.Doc.tag_remove("CONSEIL", "insert linestart",
			"insert linestart + 1 lines")
			self.Doc.tag_remove("AUTEUR", "insert linestart",
			"insert linestart + 1 lines")
		except:
			pass
		self.Doc.delete("insert -1c", "insert")
		
	def ImageWeb(self, toto=0):
		urlImage = self.frame.clipboard_get()
		lienFaux = 0
		
		protocoles = ["http://", "https://", "ftp://", "sftp://"]
		for protocole in protocoles:
			if re.search("^"+protocole, urlImage) != None and \
			re.search("(jpg)|(jpeg)|(png)|(webp)|(bmp)|(tif)|(tiff)|(gif)|\
			(eps)|(ppm)|(xbm)|(im)|(msp)|(pcx)|(spi)\.$", urlImage) != None:

				urlImage.replace("/", "")
				listeImage = urlImage.rsplit('.', 1)
				nouveauNomImage = str(int(time.time()))+"."+listeImage[1]
		
				try:
					HTTPimage = urllib.request.urlopen(urlImage)

					fichier = open("./Images/"+nouveauNomImage, "wb")
					fichier.write(HTTPimage.read())
					fichier.close()
			
					self.image.append(ImageTk.PhotoImage(Image.open("./Images/"+
					nouveauNomImage), name=nouveauNomImage))
					self.Doc.image_create(INSERT, image=self.image[-1])
					self.SauvUndoRedo()
					self.Traqueur()
				except:
					messagebox.showerror("Image introuvable", "L'adresse \
renvoie vers une ressource introuvable (erreur HTTP 404).")
			else:
				lienFaux += 1

		if lienFaux == 4:
			messagebox.showerror(message='Veuillez copier un lien dans le \
presse-papier pour insérer l\'image. \n\nLes formats suivants sont \
supportés :\n jpg, png, webp, bmp, tif, gif, eps, ppm, xbm, im, msp, pcx et \
spi.')
		
	def Image(self, toto=0):
		urlImage = askopenfilename(filetypes=[
		('Image','*.jpg'), ('Image','*.jpeg'), ('Image','*.png'),
		('Image','*.webp'), ('Image','*.bmp'), ('Image','*.tif'),
		('Image','*.tiff'), ('Image','*.gif'), ('Image','*.eps'),
		('Image','*.ppm'), ('Image','*.xbm'), ('Image','*.im'),
		('Image','*.msp'), ('Image','*.pcx'), ('Image','*.spi'),
		('Image JPEG','*.jpg'), ('Image JPEG','*.jpeg'), ('Image PNG','*.png'),
		('Image WEBP','*.webp'), ('Image BMP','*.bmp'), ('Image TIFF','*.tif'),
		('Image TIFF','*.tiff'), ('Image GIF','*.gif'), ('Image EPS','*.eps'),
		('Image PPM','*.ppm'), ('Image XBM','*.xbm'), ('Image IM','*.im'),
		('Image MSP','*.msp'), ('Image PCX','*.pcx'), ('Image SPIDER','*.spi')
		],
		initialdir=os.path.expanduser('~'), title='Importer une image')

		if urlImage:
			listeImage = urlImage.rsplit('.', 1)
			nouveauNomImage = str(int(time.time()))+"."+listeImage[1]
		
			shutil.copyfile(urlImage, "./Images/"+nouveauNomImage)
		
			self.image.append(ImageTk.PhotoImage(Image.open("./Images/"+
			nouveauNomImage), name=nouveauNomImage))
			self.Doc.image_create(INSERT, image=self.image[-1])
			self.SauvUndoRedo()
			self.Traqueur()

	def CreerDessin(self, toto=0):
		if platform.system() == "Windows":
			nouveauNomImage = str(int(time.time()))+".png"
			
			os.system('copy '+os.path.abspath('')+'\Images\mod.png '+
			os.path.abspath('')+'\Images\\'+nouveauNomImage)
			
			os.system('mspaint '+os.path.abspath('')+'\Images\\'+
			nouveauNomImage)
			
			self.image.append(ImageTk.PhotoImage(
			Image.open(".\Images\\"+nouveauNomImage), name=nouveauNomImage))
			
			self.Doc.image_create(INSERT, image=self.image[-1])

			self.SauvUndoRedo()
			self.Traqueur()
		elif platform.system() == "Linux":
			if os.path.isfile("/usr/bin/xpaint"):
				nouveauNomImage = str(int(time.time()))+".png"
				
				os.system('cp '+os.path.abspath('')+'/Images/mod.png '+
				os.path.abspath('')+'/Images/'+nouveauNomImage)
				
				os.system('xpaint '+os.path.abspath('')+'/Images/'+
				nouveauNomImage)
				
				self.image.append(ImageTk.PhotoImage(Image.open("./Images/"+
				nouveauNomImage), name=nouveauNomImage))
				
				self.Doc.image_create(INSERT, image=self.image[-1])

				self.SauvUndoRedo()
				self.Traqueur()
			else:
				messagebox.showerror("Application XPaint introuvable", "\
L'application XPaint est nécessaire pour créer des dessins. Elle est disponible \
dans les dépôts de nombreuses distributions.")
		elif platform.system() == "Darwin":
			if os.path.isfile("/Applications/Paintbrush"):
				nouveauNomImage = str(int(time.time()))+".png"
				
				os.system('cp '+os.path.abspath('')+'/Images/mod.png '+
				os.path.abspath('')+'/Images/'+nouveauNomImage)
				
				os.system('paintbrush '+os.path.abspath('')+'/Images/'+
				nouveauNomImage)
				
				self.image.append(ImageTk.PhotoImage(Image.open("./Images/"+
				nouveauNomImage), name=nouveauNomImage))
				
				self.Doc.image_create(INSERT, image=self.image[-1])
				
				self.Traqueur()
			else:
				messagebox.showerror("Application Paintbrush introuvable", "\
L'application Paintbrush est nécessaire pour créer des dessins. Elle est \
disponible librement sur http://paintbrush.sourceforge.net")

	def SauvUndoRedo(self, toto=0):
		self.indexMaxAR += 1
		self.indexAR = self.indexMaxAR	
		self.indexPosAR.append(self.Doc.index(INSERT))
		
		fichierCode = Codeur(self.balises, self.Doc.dump(0.0, END), self.image)
		
		fichier = open("Temporaire/AnnulerRefaire/"+str(self.indexAR),
		'w', encoding='utf-8')
		fichier.write(fichierCode)
		fichier.close()

	def SauvFuturUndoRedo(self, toto=0):
		self.indexPosAR.append(self.Doc.index(INSERT))
		
		fichierCode = Codeur(self.balises, self.Doc.dump(0.0, END), self.image)
		
		fichier = open("Temporaire/AnnulerRefaire/"+str(self.indexAR),
		'w', encoding='utf-8')
		fichier.write(fichierCode)
		fichier.close()

	def Enr(self, toto=0):
		fichierCode = Codeur(self.balises, self.Doc.dump(0.0, END), self.image)
		self.fichierVerif = fichierCode
		
		fichier = open(self.cheminFichier, 'w', encoding='utf-8')
		fichier.write(fichierCode)
		fichier.close()
		
		self.Traqueur()

	def Suppr(self):
		self.Doc.delete(SEL_FIRST,SEL_LAST)

	def Copier(self):
		self.frame.clipboard_clear()
		self.frame.clipboard_append(self.Doc.get(SEL_FIRST, SEL_LAST))

	def Couper(self):
		self.Copier()
		self.Doc.delete(SEL_FIRST, SEL_LAST)
		self.SauvUndoRedo()

	def Coller(self):
		pressePapiers = self.frame.clipboard_get()
		protocoles = ["http://", "https://", "ftp://", "sftp://"]
		for protocole in protocoles:
			if re.search(protocole, pressePapiers) != None:
				pressePapiers = pressePapiers+" "
	
		try:
			self.Doc.delete(SEL_FIRST, SEL_LAST)
			self.Doc.insert(INSERT, pressePapiers)
		except:
			self.Doc.insert(INSERT, pressePapiers)
			
		self.GenLiens()
		self.SauvUndoRedo()
			
		#imageCollee = self.image.append(ImageTk.PhotoImage(imageCollee,
		#name=str(int(time.time()))))
		#self.Doc.image_create(INSERT, image=self.image[-1])

	def BaliseMode(self, balise):
		if balise == "GRAS":
			enfonce = self.Gras_check.get()
		elif balise == "CODE":
			enfonce = self.Code_check.get()
			
		# Si du texte est sélectionné
		try:
			 # S'il est en balisé
			if balise in self.Doc.tag_names("sel.first"):
				self.Doc.tag_remove(balise, "sel.first", "sel.last")
			# Sinon, s'il est normal
			else:
				if self.Doc.get("sel.last") == "\n": 
					self.Doc.tag_add(balise, "sel.first",
					"sel.last +1l linestart")
				else:
					self.Doc.tag_add(balise, "sel.first", "sel.last")
			self.SauvUndoRedo()
			self.Traqueur()
					
		# Si aucune sélection n'est faite
		except:
			prochainCarac = self.Doc.get(INSERT, "insert +1c")
			caracApresMot = self.Doc.get("insert wordend", "insert wordend +1c")
			
			# Si le curseur est entre deux mots
			if prochainCarac == " " or prochainCarac == "\n" or\
			prochainCarac == "\t":
				# Si le curseur est sur du balisé
				if enfonce == 1:
					def LettreTapee(touche=""):	
						if caracApresMot == "\n":
							self.Doc.tag_remove(balise, "insert -1c",
							"insert +1l linestart")
						else:
							self.Doc.tag_remove(balise, "insert -1c",
							"insert wordend")

					self.Doc.bind("<KeyRelease>", LettreTapee)

					self.SauvUndoRedo()
					self.Traqueur(forcer=balise)

				# Sinon si le curseur est sur du texte normal
				else:
					def LettreTapee(touche=""):
						if caracApresMot == "\n":
							self.Doc.tag_add(balise, "insert -1c",
							"insert +1l linestart")
						else:
							self.Doc.tag_add(balise, "insert -1c",
							"insert wordend")

					self.Doc.bind("<KeyRelease>", LettreTapee)

					self.SauvUndoRedo()
					self.Traqueur(forcer=balise, pos=True)

			# Si le curseur est dans un mot
			else:
				if balise in self.Doc.tag_names("insert"):
					if caracApresMot == "\n":
						self.Doc.tag_remove(balise, "insert wordstart",
						"insert +1l linestart")
					else:
						self.Doc.tag_remove(balise, "insert wordstart",
						"insert wordend")
				else:
					if caracApresMot == "\n":
						self.Doc.tag_add(balise, "insert wordstart",
						"insert +1l linestart")
					else:
						self.Doc.tag_add(balise, "insert wordstart",
						"insert wordend +1c")
				self.SauvUndoRedo()
				self.Traqueur()
				
		self.SauvUndoRedo()
			
	def Gras(self, toto=0):
		self.BaliseMode("GRAS")
				
	def Code(self, toto=0):
		self.BaliseMode("CODE")

	def SurlignRien(self, toto=0):
		couleurs = ["JAUNE", "VERT", "BLEU"]
		for i in couleurs:
			try:
				self.Doc.tag_remove(i, "sel.first", "sel.last")
			except:  
				self.Doc.tag_remove(i, "insert wordstart", "insert wordend")
		self.SauvUndoRedo()
		self.Traqueur()
		
	def SurlignJaune(self, toto=0):
		self.SurlignRien()
		try:
			self.Doc.tag_add("JAUNE", "sel.first", "sel.last")
		except:  
			self.Doc.tag_add("JAUNE", "insert wordstart", "insert wordend")
		self.SauvUndoRedo()
		self.Traqueur()

	def SurlignVert(self, toto=0):
		self.SurlignRien()
		try:
			self.Doc.tag_add("VERT", "sel.first", "sel.last")
		except:  
			self.Doc.tag_add("VERT", "insert wordstart", "insert wordend")
		self.SauvUndoRedo()
		self.Traqueur()

	def SurlignBleu(self, toto=0):
		self.SurlignRien()
		try:
			self.Doc.tag_add("BLEU", "sel.first", "sel.last")
		except:  
			self.Doc.tag_add("BLEU", "insert wordstart", "insert wordend")
		self.SauvUndoRedo()
		self.Traqueur()

	def SupprFormatage(self, toto=0):
		for i in self.Doc.tag_names():
			if not i == "sel":
				try:
					self.Doc.tag_remove(i, "sel.first", "sel.last")
				except:
					self.Doc.tag_remove(i, "0.0", END)
		self.SauvUndoRedo()

	def ToutSel(self):
		self.Doc.focus_set()
		self.Doc.tag_add("sel", "0.0", END)
	
	def TypePar(self, toto=0):	
		def effacerAutresStyles():
			try:
				self.Doc.tag_remove("T1", "insert linestart",
				"insert linestart + 1 lines")
				self.Doc.tag_remove("T2", "insert linestart",
				"insert linestart + 1 lines")
				self.Doc.tag_remove("T3", "insert linestart",
				"insert linestart + 1 lines")
				self.Doc.tag_remove("T4", "insert linestart",
				"insert linestart + 1 lines")
				self.Doc.tag_remove("CITATION", "insert linestart",
				"insert linestart + 1 lines")
				self.Doc.tag_remove("AVERTISSEMENT", "insert linestart",
				"insert linestart + 1 lines")
				self.Doc.tag_remove("CONSEIL", "insert linestart",
				"insert linestart + 1 lines")
				self.Doc.tag_remove("AUTEUR", "insert linestart",
				"insert linestart + 1 lines")
			except:
				pass
				
		if self.choixTypePar.get() != "Paragraphe":
		
			if "Titre 1" or "Titre 2" or "Titre 3" or "Titre 4"\
			or "Citation" or "Avertissement" or "Conseil" or "Source"\
			in self.Doc.tag_names("insert"):
				effacerAutresStyles()
				
			if self.choixTypePar.get() == "Titre 1":
				self.Doc.tag_add("T1", "insert linestart",
				"insert linestart + 1 lines")
				self.Styles_check.set(1)
			elif self.choixTypePar.get() == "Titre 2":
				self.Doc.tag_add("T2", "insert linestart",
				"insert linestart + 1 lines")
				self.Styles_check.set(2)
			elif self.choixTypePar.get() == "Titre 3":
				self.Doc.tag_add("T3", "insert linestart",
				"insert linestart + 1 lines")
				self.Styles_check.set(3)
			elif self.choixTypePar.get() == "Titre 4":
				self.Doc.tag_add("T4", "insert linestart",
				"insert linestart + 1 lines")
				self.Styles_check.set(4)
			elif self.choixTypePar.get() == "Citation":
				self.Doc.tag_add("CITATION", "insert linestart",
				"insert linestart + 1 lines")
				self.Styles_check.set(5)
			elif self.choixTypePar.get() == "Avertissement":
				self.Doc.tag_add("AVERTISSEMENT", "insert linestart",
				"insert linestart + 1 lines")
				self.Styles_check.set(6)
			elif self.choixTypePar.get() == "Conseil":
				self.Doc.tag_add("CONSEIL", "insert linestart",
				"insert linestart + 1 lines")
				self.Styles_check.set(7)
			elif self.choixTypePar.get() == "Source":
				self.Doc.tag_add("AUTEUR", "insert linestart",
				"insert linestart + 1 lines")
				self.Styles_check.set(8)
				
		else:
			effacerAutresStyles()
			self.Styles_check.set(0)
		self.SauvUndoRedo()
		self.Traqueur()
			
	def MenuContextuel(self,event):
		try:
			self.menu.destroy()
		except:
			pass
			
		self.menu = Menu(tearoff=0)
		self.menu.add_command(label="Couper", command=self.Couper)
		self.menu.add_command(label="Copier", command=self.Copier)
		self.menu.add_command(label="Coller", command=self.Coller)
		self.menu.add_command(label="Insérer l'image du Web",
		command=self.ImageWeb)
		self.menu.add_separator()
		self.menu.add_command(label="Supprimer", command=self.Suppr)
		
		try:
			self.frame.clipboard_get()
		except:
			self.menu.entryconfigure(2, state='disabled')
			
		try:
			self.Doc.get(SEL_FIRST, SEL_LAST)
		except:
			self.menu.entryconfigure(0, state='disabled')
			self.menu.entryconfigure(1, state='disabled')
			self.menu.entryconfigure(5, state='disabled')
			
		if self.cheminFichier == "":
			self.menu.entryconfigure(0, state='disabled')
			self.menu.entryconfigure(2, state='disabled')
			self.menu.entryconfigure(3, state='disabled')
			self.menu.entryconfigure(5, state='disabled')
			
		try:
			urlImage = self.frame.clipboard_get()
			protocoles = ["http://", "https://", "ftp://", "sftp://"]
			for protocole in protocoles:
				if re.search("^http://", urlImage) == None or \
				re.search("(jpg)|(jpeg)|(png)|(webp)|(bmp)|(tif)|(tiff)|(gif)|\
				(eps)|(ppm)|(xbm)|(im)|(msp)|(pcx)|(spi)\.$", urlImage) == None:
					self.menu.entryconfigure(3, state='disabled')
		except:
			self.menu.entryconfigure(3, state='disabled')
			
		self.menu.post(event.x_root, event.y_root)
	
	def EffacerMenu(self,event):
		try:
			self.menu.destroy()
		except:
			pass

	def GenLiens(self, toto=0):
		protocoles = ["http://", "https://", "ftp://", "sftp://"]
		for protocole in protocoles:
			chaineDoc = self.Doc.get(0.0, END)
			debutLien = '0.0'
			finLien = '0.0'
		
			i = 0
			while i < chaineDoc.count(protocole):
				debutLien = self.Doc.search(protocole, debutLien+'+1c')
				finLien = self.Doc.search(" ", debutLien)
				self.Doc.tag_add("LIEN", debutLien, finLien)
				i += 1		

	def InfosBarreEtat(self, ouverture=False):
		document = self.Doc.get(0.0, END)
		
		self.nbLignes.configure(text=str(len(document.split('\n'))-1))
		self.nbMots.configure(text=str(len(document.split())))
		if ouverture == True:
			self.pos.configure(text='0.0')
		else:
			self.pos.configure(text=self.Doc.index(INSERT))

	def Traqueur(self, toto=0, forcer="", pos=False):
		# Icône de sauvegarde
		if Codeur(self.balises, self.Doc.dump(0.0, END), self.image) !=\
		self.fichierVerif:
			self.boutonEnr.config(image=self.i2)
			self.etatSauv.configure(text="Modifications non enregistrées !")
		else:
			self.boutonEnr.config(image=self.i1)
			self.etatSauv.configure(text="Enregistré")
			
		if forcer == "":
			self.Doc.unbind("<KeyRelease>")
			self.Doc.bind("<KeyRelease>", self.Traqueur)

		# Undo Redo
		if self.indexAR == 0:
			self.boutonUndo.configure(state=DISABLED)
		else:
			self.boutonUndo.configure(state=NORMAL)

		if self.indexAR == self.indexMaxAR:
			self.boutonRedo.configure(state=DISABLED)
		else:
			self.boutonRedo.configure(state=NORMAL)
			
		# Méthodes de gestion des boutons de barre d'outil ou de menu
		def ActiverGras():
			self.boutonGras.configure(relief=SUNKEN, overrelief=SUNKEN)
			self.Gras_check.set(1)
			
		def DesactiverGras():
			self.boutonGras.configure(relief=FLAT, overrelief=RAISED)
			self.Gras_check.set(0)
			
		def ActiverCode():
			self.boutonCode.configure(relief=SUNKEN, overrelief=SUNKEN)
			self.Code_check.set(1)
			
		def DesactiverCode():
			self.boutonCode.configure(relief=FLAT, overrelief=RAISED)
			self.Code_check.set(0)
			
		# Mise en force de bouton
		if forcer=="GRAS":
			if pos==True: ActiverGras()
			else: DesactiverGras()
			
		if forcer=="CODE":
			if pos==True: ActiverCode()
			else: DesactiverCode()

		# Sinon, gestion automatique de l'état des boutons
		try:
			if forcer != "GRAS":
				if "GRAS" in self.Doc.tag_names("insert"):
					ActiverGras()
				else:
					DesactiverGras()
				
			if forcer != "CODE":
				if "CODE" in self.Doc.tag_names("insert"):
					ActiverCode()
				else:
					DesactiverCode()

			if "JAUNE" in self.Doc.tag_names("insert"):
				self.boutonSurlignRien.configure(relief=FLAT, overrelief=RAISED)
				self.boutonSurlignJaune.configure(relief=SUNKEN,
				overrelief=SUNKEN)
				self.boutonSurlignVert.configure(relief=FLAT, overrelief=RAISED)
				self.boutonSurlignBleu.configure(relief=FLAT, overrelief=RAISED)
				self.Surligner_check.set(1)
			elif "VERT" in self.Doc.tag_names("insert"):
				self.boutonSurlignRien.configure(relief=FLAT, overrelief=RAISED)
				self.boutonSurlignJaune.configure(relief=FLAT,
				overrelief=RAISED)
				self.boutonSurlignVert.configure(relief=SUNKEN,
				overrelief=SUNKEN)
				self.boutonSurlignBleu.configure(relief=FLAT, overrelief=RAISED)
				self.Surligner_check.set(2)
			elif "BLEU" in self.Doc.tag_names("insert"):
				self.boutonSurlignRien.configure(relief=FLAT, overrelief=RAISED)
				self.boutonSurlignJaune.configure(relief=FLAT,
				overrelief=RAISED)
				self.boutonSurlignVert.configure(relief=FLAT, overrelief=RAISED)
				self.boutonSurlignBleu.configure(relief=SUNKEN,
				overrelief=SUNKEN)
				self.Surligner_check.set(3)
			else:
				self.boutonSurlignRien.configure(relief=FLAT, overrelief=RAISED)
				self.boutonSurlignJaune.configure(relief=FLAT,
				overrelief=RAISED)
				self.boutonSurlignVert.configure(relief=FLAT, overrelief=RAISED)
				self.boutonSurlignBleu.configure(relief=FLAT, overrelief=RAISED)
				self.Surligner_check.set(0)

		except:
			pass
			
		if "T1" in self.Doc.tag_names("insert"):
			self.choixTypePar.set("Titre 1")
			self.Styles_check.set(1)
		elif "T2" in self.Doc.tag_names("insert"):
			self.choixTypePar.set("Titre 2")
			self.Styles_check.set(2)
		elif "T3" in self.Doc.tag_names("insert"):
			self.choixTypePar.set("Titre 3")
			self.Styles_check.set(3)
		elif "T4" in self.Doc.tag_names("insert"):
			self.choixTypePar.set("Titre 4")
			self.Styles_check.set(4)
		elif "CITATION" in self.Doc.tag_names("insert"):
			self.choixTypePar.set("Citation")
			self.Styles_check.set(5)
		elif "AVERTISSEMENT" in self.Doc.tag_names("insert"):
			self.choixTypePar.set("Avertissement")
			self.Styles_check.set(6)
		elif "CONSEIL" in self.Doc.tag_names("insert"):
			self.choixTypePar.set("Conseil")
			self.Styles_check.set(7)
		elif "AUTEUR" in self.Doc.tag_names("insert"):
			self.choixTypePar.set("Source")
			self.Styles_check.set(8)
		else:
			self.choixTypePar.set("Paragraphe")
			self.Styles_check.set(0)

			
