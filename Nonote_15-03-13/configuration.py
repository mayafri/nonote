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
import platform, tkinter.font

def RechargerConf(self):
	self.ChargerConf()
	
	self.ObjDoc.Police.config(size=self.texte_taille)
	self.ObjDoc.Police.config(family=self.texte_police)
	
	self.ObjDoc.PoliceGras.config(size=self.texte_taille)
	self.ObjDoc.PoliceGras.config(family=self.texte_police)

	self.ObjDoc.PoliceT1.config(size=int(self.texte_taille*2.5))
	self.ObjDoc.PoliceT1.config(family=self.texte_police)
	
	self.ObjDoc.PoliceT2.config(size=int(self.texte_taille*2))
	self.ObjDoc.PoliceT2.config(family=self.texte_police)

	self.ObjDoc.PoliceT3.config(size=int(self.texte_taille*1.6))
	self.ObjDoc.PoliceT3.config(family=self.texte_police)
	
	self.ObjDoc.PoliceT4.config(size=int(self.texte_taille*1.3))
	self.ObjDoc.PoliceT4.config(family=self.texte_police)
	
	self.ObjDoc.PoliceCite.config(size=self.texte_taille)
	self.ObjDoc.PoliceCite.config(family=self.texte_police)
	
	self.ObjDoc.PoliceAuteur.config(size=int(self.texte_taille/1.5))
	self.ObjDoc.PoliceAuteur.config(family=self.texte_police)
	
	self.ObjDoc.PoliceCode.config(size=str(int(self.texte_taille)-1))
	
	self.ObjDoc.TexteTailleDefaut = self.texte_taille

	self.ObjDoc.CouleurFond(self.couleur_fond)
	self.ObjDoc.Doc.config(width=self.largeur_texte)

class ClasseConf():
	def __init__(self):
		self.FConfig = Toplevel()
		self.FConfig.grab_set()
	
		conf = open("Special/config.txt", 'r', encoding='utf-8')

		conf_str = conf.read()
		conf_str = re.sub('\n*', '', conf_str)

		self.texte_taille = re.sub('.*<TEXTE_TAILLE>', '', conf_str)
		self.texte_taille = re.sub('</TEXTE_TAILLE>.*', '', self.texte_taille)
		self.texte_police = re.sub('.*<TEXTE_POLICE>', '', conf_str)
		self.texte_police = re.sub('</TEXTE_POLICE>.*', '', self.texte_police)
		self.couleur_fond = re.sub('.*<COULEUR_FOND>', '', conf_str)
		self.couleur_fond = re.sub('</COULEUR_FOND>.*', '', self.couleur_fond)
		self.largeur_texte = re.sub('.*<LARGEUR_TEXTE>', '', conf_str)
		self.largeur_texte = re.sub('</LARGEUR_TEXTE>.*', '',
		self.largeur_texte)

		conf.close()
		
		self.radioPolice = IntVar()

		self.framePolice = ttk.LabelFrame(self.FConfig, text="Texte")
		self.framePage = ttk.LabelFrame(self.FConfig, text="Page")

		self.boutonAppliquer = ttk.Button(self.FConfig, text="Appliquer")
		self.boutonOK = ttk.Button(self.FConfig, text="OK")

		self.FenConf()

	def EnrConf(self):
			conf = open("Special/config.txt", 'r', encoding='utf-8')
			conf_str = conf.read()
			
			if self.radioPolice.get() == 1:
				conf_str = re.sub('<TEXTE_POLICE>.*</TEXTE_POLICE>',
				'<TEXTE_POLICE>Helvetica</TEXTE_POLICE>', conf_str)
			elif self.radioPolice.get() == 2:
				conf_str = re.sub('<TEXTE_POLICE>.*</TEXTE_POLICE>',
				'<TEXTE_POLICE>Times</TEXTE_POLICE>', conf_str)
			else:
				conf_str = re.sub('<TEXTE_POLICE>.*</TEXTE_POLICE>',
				'<TEXTE_POLICE>'+self.choixPolice.get()+'</TEXTE_POLICE>',
				conf_str)
			conf_str = re.sub('<TEXTE_TAILLE>.*</TEXTE_TAILLE>',
			'<TEXTE_TAILLE>'+self.choixTaille.get()+'</TEXTE_TAILLE>',
			conf_str)
			conf_str = re.sub('<COULEUR_FOND>.*</COULEUR_FOND>',
			'<COULEUR_FOND>'+self.choixFond.get()+'</COULEUR_FOND>',
			conf_str)
			conf_str = re.sub('<LARGEUR_TEXTE>.*</LARGEUR_TEXTE>',
			'<LARGEUR_TEXTE>'+self.choixLargeur.get()+'</LARGEUR_TEXTE>',
			conf_str)

			conf = open("Special/config.txt", 'w', encoding='utf-8')
			conf.write(conf_str)
			conf.close()

	def FenConf(self):
		def PoliceCheckWidget():
			if self.radioPolice.get() == 3:
				self.choixPolice.configure(state='readonly')
			else:
				self.choixPolice.configure(state='disabled')
			
		textePolice = ttk.Label(self.framePolice, text="Police :")

		choixPoliceListe = list(font.families())
		
		radio1 = ttk.Radiobutton(self.framePolice, text="Sans",
		variable=self.radioPolice, value=1, command=PoliceCheckWidget)
		radio2 = ttk.Radiobutton(self.framePolice, text="Serif",
		variable=self.radioPolice, value=2, command=PoliceCheckWidget)
		
		radio3 = ttk.Radiobutton(self.framePolice, text="Police personnalisée",
		variable=self.radioPolice, value=3, command=PoliceCheckWidget)	
		self.choixPolice = ttk.Combobox(self.framePolice,
		values=choixPoliceListe, state='disabled')
		
		if self.texte_police == "Helvetica":
			self.radioPolice.set("1")
		elif self.texte_police == "Times":
			self.radioPolice.set("2")
		else:
			self.radioPolice.set("3")
			self.choixPolice.configure(state='readonly')
		for i in choixPoliceListe:
			if self.texte_police == i:
				self.choixPolice.set(i)
	
		texteTaille = ttk.Label(self.framePolice, text="Taille :")

		choixTailleListe = ["6", "7", "8", "9", "10", "11", "12", "13", "14",
		"15", "16", "17", "18", "19", "20"]

		self.choixTaille = ttk.Combobox(self.framePolice,
		values=choixTailleListe, state='readonly')

		for i in choixTailleListe:
			if self.texte_taille == i:
				self.choixTaille.set(i)

		texteFond = ttk.Label(self.framePage, text="Couleur de fond :")

		choixFondListe = ["Blanc", "Gris", "Jaune", "Vert", "Bleu", "Mauve"]

		self.choixFond = ttk.Combobox(self.framePage, values=choixFondListe,
		state='readonly')

		for i in choixFondListe:
			if self.couleur_fond == i:
				self.choixFond.set(i)
				
		texteLargeur = ttk.Label(self.framePage, text="Largeur de page :")

		choixLargeurListe = ["50", "60", "70", "80", "90", "100", "110", "120",
		"130"]

		self.choixLargeur = ttk.Combobox(self.framePage,
		values=choixLargeurListe, state='readonly')

		for i in choixLargeurListe:
			if self.largeur_texte == i:
				self.choixLargeur.set(i)
		
		textePolice.grid(row=0, column=0, sticky="W")
		radio1.grid(row=0, column=1, sticky="WE", padx=3, pady=3)
		radio2.grid(row=1, column=1, sticky="WE", padx=3, pady=3)
		radio3.grid(row=2, column=1, sticky="WE", padx=3, pady=3)
		self.choixPolice.grid(row=3, column=1, sticky="E", padx=3, pady=3)
		texteTaille.grid(row=4, column=0, sticky="W")
		self.choixTaille.grid(row=4, column=1, sticky="E", padx=3, pady=3)

		self.framePolice.columnconfigure(0,weight=1)
		
		texteFond.grid(row=0, column=0, sticky="W")
		self.choixFond.grid(row=0, column=1, sticky="E", padx=3, pady=3)
		texteLargeur.grid(row=1, column=0, sticky="W")
		self.choixLargeur.grid(row=1, column=1, sticky="E", padx=3, pady=3)

		self.framePage.columnconfigure(0,weight=1)
		
		if platform.system() == "Windows":
			self.FConfig.iconbitmap('Icones\logo.ico')

		self.FConfig.title("Configuration")
		self.FConfig.resizable(False,False)

		boutonAnnuler = ttk.Button(self.FConfig, text="Annuler",
		command=self.FConfig.destroy)

		self.framePolice.grid(row=0, column=0, columnspan=3,
		sticky="NSEW", padx=6, pady=6)
		self.framePage.grid(row=1, column=0, columnspan=3,
		sticky="NSEW", padx=6, pady=6)

		boutonAnnuler.grid(row=2, column=2, padx=6, pady=6)
		self.boutonAppliquer.grid(row=2, column=0, padx=6, pady=6)
		self.boutonOK.grid(row=2, column=1, padx=6, pady=6)

