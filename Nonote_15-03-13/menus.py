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
import platform
from guide import *
from utilitaire import *
from convertisseur_html import *
from convertisseur_pdf import *
from convertisseur_txt import *
from a_propos import *
from configuration import *
from PIL import Image, ImageTk
from codeur import *

def barreMenus(self):	
	def PleinEcran(toto=0):
		if self.f_full == 0:
			self.fenetre.attributes('-fullscreen', True)
			self.f_full = 1
			self.f_full_check.set(1)
			pleinecran.configure(relief=SUNKEN, overrelief=SUNKEN)
		else:
			self.fenetre.attributes('-fullscreen', False)
			self.f_full = 0
			self.f_full_check.set(0)
			pleinecran.configure(relief=FLAT, overrelief=RAISED)
	
	def ExploAvancee(toto=0):
		if platform.system() == "Darwin":
			os.system("open \""+self.ObjNav.racine+"\"")
		elif platform.system() == "Windows":
			os.system("Explorer.exe /root,"+os.path.abspath(self.ObjNav.racine))
		elif platform.system() == "Linux":
			os.system("xdg-open \""+self.ObjNav.racine+"\"")
			
	def Fermer():
		self.DocOuvrir(fermer=True)
		
	def ToutSel(toto=0):
		self.ObjDoc.ToutSel()
		
	def ExporterHTML(toto=0):
		fichier = Codeur(self.ObjDoc.balises, self.ObjDoc.Doc.dump(0.0, END),
		self.ObjDoc.image)
		
		ConvHTML(fichier, CheminBeau(self.ObjDoc.cheminFichier))
		
	def Imprimer():
		fichier = Codeur(self.ObjDoc.balises, self.ObjDoc.Doc.dump(0.0, END),
		self.ObjDoc.image)
		
		numero = str(int(time.time()))
		
		ConvHTML(fichier, CheminBeau(self.ObjDoc.cheminFichier),
		police=self.texte_police, auto=numero)
		
		os.system("./Utilitaires/wkhtmltopdf "+os.path.abspath('')+\
		"/Temporaire/"+numero+".html "+os.path.abspath('')+\
		"/Temporaire/"+numero+".pdf")
		
	def ExporterPDF(toto=0):
		ConvPDF(self)

	def ExporterTXT(toto=0):
		fichier = Codeur(self.ObjDoc.balises, self.ObjDoc.Doc.dump(0.0, END),
		self.ObjDoc.image)
		
		ConvTXT(fichier, CheminBeau(self.ObjDoc.cheminFichier), self.ObjDoc.balises)

	def AProposRelais(toto=0):
		APropos(self)

	def ConfRelais(toto=0):
		ObjConf = ClasseConf()
		
		def Ok():
			ObjConf.EnrConf()
			RechargerConf(self)
			ObjConf.FConfig.destroy()
		def Appliquer():
			ObjConf.EnrConf()
			RechargerConf(self)
			
		ObjConf.boutonOK.configure(command=Ok)
		ObjConf.boutonAppliquer.configure(command=Appliquer)

	def RelaisGuide(toto=0):
		Guide(self)
		
	if platform.system() == "Darwin":
		menubar = Menu(self.fenetre)

		apple = Menu(menubar, name='apple', tearoff=0)
		apple.add_command(label="À propos de Nonote", command=AProposRelais)
		apple.add_separator()
		apple.add_command(label="Préférences...", command=ConfRelais)
		apple.add_command(label="Exploration avancée...", command=ExploAvancee)

		menubar.add_cascade(label="Nonote", menu=apple)
		
		self.fenetre.config(menu=menubar)
	
	self.iBarre1 = ImageTk.PhotoImage(Image.open('Icones/exploav.png'))
	self.iBarre13 = ImageTk.PhotoImage(Image.open('Icones/txt.png'))
	self.iBarre2 = ImageTk.PhotoImage(Image.open('Icones/exporthtml.png'))
	self.iBarre12 = ImageTk.PhotoImage(Image.open('Icones/pdf.png'))
	self.iBarre11 = ImageTk.PhotoImage(Image.open('Icones/imprimer.png'))
	self.iBarre3 = ImageTk.PhotoImage(Image.open('Icones/toutSel.png'))
	self.iBarre10 = ImageTk.PhotoImage(Image.open('Icones/PleinEcran.png'))	
	self.iBarre5 = ImageTk.PhotoImage(Image.open('Icones/apropos.png'))
	self.iBarre6 = ImageTk.PhotoImage(Image.open('Icones/guide.png'))
	self.iBarre7 = ImageTk.PhotoImage(Image.open('Icones/prefs.png'))	
	self.iBarre8 = ImageTk.PhotoImage(Image.open('Icones/fermer.png'))
	self.iBarre9 = ImageTk.PhotoImage(Image.open('Icones/quitter.png'))
	
	Barre = Frame()

	self.BMexportTXT = Button(Barre, overrelief=RAISED, relief=FLAT,
	image=self.iBarre13)
	
	self.BMexportTXT.pack(side=LEFT)
	self.BMexportTXT.configure(command=ExporterTXT)

	self.BMexport = Button(Barre, overrelief=RAISED, relief=FLAT,
	image=self.iBarre2)
	
	self.BMexport.pack(side=LEFT)
	self.BMexport.configure(command=ExporterHTML)
	
	self.BMexportPDF = Button(Barre, overrelief=RAISED, relief=FLAT,
	image=self.iBarre12)
	
	self.BMexportPDF.pack(side=LEFT)
	self.BMexportPDF.configure(command=ExporterPDF)
	
	self.BMimprimer = Button(Barre, overrelief=RAISED, relief=FLAT,
	image=self.iBarre11)
	
	#self.BMimprimer.pack(side=LEFT)
	self.BMimprimer.configure(command=Imprimer)
	
	ttk.Separator(Barre,orient=VERTICAL).pack(side=LEFT, fill=BOTH)
	
	toutSel = Button(Barre, overrelief=RAISED, relief=FLAT, image=self.iBarre3)
	toutSel.pack(side=LEFT)
	toutSel.configure(command=ToutSel)
	
	ttk.Separator(Barre,orient=VERTICAL).pack(side=LEFT, fill=BOTH)
	
	pleinecran = Button(Barre, overrelief=RAISED, relief=FLAT,
	image=self.iBarre10)
	
	pleinecran.pack(side=LEFT)
	pleinecran.configure(command=PleinEcran)
	
	ttk.Separator(Barre,orient=VERTICAL).pack(side=LEFT, fill=BOTH)
	
	exploav = Button(Barre, overrelief=RAISED, relief=FLAT,
	image=self.iBarre1)
	
	exploav.pack(side=LEFT)
	exploav.configure(command=ExploAvancee)
	
	prefs = Button(Barre, overrelief=RAISED, relief=FLAT, image=self.iBarre7)
	prefs.pack(side=LEFT)
	prefs.configure(command=ConfRelais)
	
	ttk.Separator(Barre,orient=VERTICAL).pack(side=LEFT, fill=BOTH)	
	
	guide = Button(Barre, overrelief=RAISED, relief=FLAT, image=self.iBarre6)
	guide.pack(side=LEFT)
	guide.configure(command=RelaisGuide)
	
	apropos = Button(Barre, overrelief=RAISED, relief=FLAT, image=self.iBarre5)
	apropos.pack(side=LEFT)
	apropos.configure(command=AProposRelais)

	ttk.Separator(Barre,orient=VERTICAL).pack(side=LEFT, fill=BOTH)

	quitter = Button(Barre, overrelief=RAISED, relief=FLAT, image=self.iBarre9)
	quitter.pack(side=LEFT)
	quitter.configure(command=self.ActionFermer)
	
	ttk.Separator(Barre,orient=VERTICAL).pack(side=LEFT, fill=BOTH)

	self.BMfermer = Button(Barre, image=self.iBarre8, relief=FLAT,
	overrelief=RAISED)	
	self.BMfermer.pack(side=RIGHT)
	self.BMfermer.configure(command=Fermer)

	Barre.grid(row=0, column=1, sticky=NSEW)

	# Raccourcis clavier
	
	self.fenetre.bind("<Control-q>", self.ActionFermer)
	self.fenetre.bind("<Control-Q>", self.ActionFermer)
	self.fenetre.bind("<Control-a>", ToutSel)
	self.fenetre.bind("<Control-A>", ToutSel)
	
	self.fenetre.bind("<F11>", PleinEcran)
	
	self.fenetre.bind("<F1>", RelaisGuide)
	self.fenetre.bind("<F2>", AProposRelais)
	self.fenetre.bind("<F3>", ConfRelais)
	self.fenetre.bind("<F4>", ExploAvancee)
	
	self.fenetre.bind("<F5>", ExporterTXT)
	self.fenetre.bind("<F6>", ExporterHTML)
	self.fenetre.bind("<F7>", ExporterPDF)
	
	self.fenetre.bind("<F11>", PleinEcran)
	
	
	
	
