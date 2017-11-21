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
from codeur import *
from convertisseur_html import *
from utilitaire import *
import os, time, platform, subprocess
import tkinter.messagebox as messagebox

def ConvPDF(self):
	# Vérifie si WkHTMLtoPDF est installé

	platforme = 32
	if sys.maxsize > 2**32:
		platforme = 64
	erreurWk = True
	
	if platform.system() == "Linux":
		if os.path.isfile("/bin/wkhtmltopdf") == True:
			erreurWk = False
			
	if platform.system() == "Darwin":
		if os.path.isfile("/bin/wkhtmltopdf") == True:
			erreurWk = False

	if platform.system() == "Windows":
		if os.path.isfile(os.environ["PROGRAMFILES"]+
		"\wkhtmltopdf\\bin\\wkhtmltopdf.exe") == True:
			erreurWk = False

	if erreurWk == True:
		messagebox.showerror(message='Le logiciel WkHTMLtoPDF est nécessaire \
pour exporter vos notes au format PDF, il n\'a cependant pas été \
détecté sur votre installation.\nTéléchargez-le en version '+str(platforme)+' bits \
et installez-le dans le répertoire par défaut.\n\nIl est disponible à l\'adresse \
http://wkhtmltopdf.org/.')

	else:
		varArborescence = IntVar()
		varPolice = IntVar()

		def Convertir(nomAuto=""):
			def policeGet():
				if varPolice.get() == 0:
					return "serif"
				elif varPolice.get() == 1:
					return "sans-serif"
				else:
					return choixPolice.get()

			MecanismeConvPDF(self, policeGet(), varArborescence.get(), nomAuto)
			if nomAuto=="":
				OptionsPDF.destroy()

		def Apercu():
			Convertir(nomAuto="apercu")
			webbrowser.open(os.path.dirname(__file__)+"/Temporaire/apercu.html")
		
		OptionsPDF = Toplevel()
		OptionsPDF.grab_set()
		OptionsPDF.title("Exporter en PDF")
		OptionsPDF.resizable(False,False)
			
		checkArbo = Checkbutton(OptionsPDF, text="Insérer l'arborescence",
		variable=varArborescence)

		def PoliceCheckWidget():
			if varPolice.get() == 2:
				choixPolice.configure(state='readonly')
				label.grid(row=4, column=0, columnspan=3, padx="5", pady="2")
			else:
				choixPolice.configure(state='disabled')
				label.grid_forget()

		choixPoliceListe = list(font.families())

		radio1 = ttk.Radiobutton(OptionsPDF, text="Police Serif \
(de type Serif Times)",
		variable=varPolice, value=0, command=PoliceCheckWidget)
		
		radio2 = ttk.Radiobutton(OptionsPDF, text="Police Sans-Serif \
(de type Helvetica ou Arial)",
		variable=varPolice, value=1, command=PoliceCheckWidget)
		
		radio3 = ttk.Radiobutton(OptionsPDF, text="Police personnalisée",
		variable=varPolice, value=2, command=PoliceCheckWidget)	

		choixPolice = ttk.Combobox(OptionsPDF,
		values=choixPoliceListe, state='disabled')

		label = Label(OptionsPDF, text="Attention, si vous publiez ce fichier, \
les autres utilisateurs\ndevront avoir la même police de caractère installée.")
		
		boutonAnnuler = ttk.Button(OptionsPDF, text="Annuler",
		command=OptionsPDF.destroy)
		boutonApercu = ttk.Button(OptionsPDF, text="Aperçu", command=Apercu)
		boutonApercu.configure(state='disabled')
		boutonOK = ttk.Button(OptionsPDF, text="Exporter", command=Convertir)

		checkArbo.grid(row=0, column=0, columnspan=3, sticky='W',
		padx="5", pady="2")
		radio1.grid(row=1, column=0, columnspan=3, sticky='W', padx="5", pady="2")
		radio2.grid(row=2, column=0, columnspan=3, sticky='W', padx="5", pady="2")
		radio3.grid(row=3, column=0, columnspan=3, sticky='W', padx="5", pady="2")
		choixPolice.grid(row=3, column=2, columnspan=1, sticky='WE',
		padx="5", pady="2")
		label.grid_forget()
		boutonAnnuler.grid(row=5, column=0, padx="5", pady="2")
		boutonApercu.grid(row=5, column=1, padx="5", pady="2")
		boutonOK.grid(row=5, column=2, padx="5", pady="2")

def MecanismeConvPDF(self, parPolice, parArbo, auto=""):
	if platform.system() == "Linux":
		fichier = Codeur(self.ObjDoc.balises, self.ObjDoc.Doc.dump(0.0, END),
		self.ObjDoc.image)
		
		numero = str(int(time.time()))
		
		MecanismeConvHTML(fichier, CheminBeau(self.ObjDoc.cheminFichier),
		police=parPolice, auto=numero, arbo=parArbo)
	
		titre = re.sub(".* » ", "", CheminBeau(self.ObjDoc.cheminFichier))
	
		destFichier = asksaveasfilename(initialfile=titre+'.pdf',
		defaultextension='.pdf', filetypes=[('Fichier PDF','*.PDF')],
		initialdir=os.path.expanduser('~'), title='Exporter en PDF')
	
		if destFichier != "" and destFichier != None:
			os.system("wkhtmltopdf '"+os.path.abspath('')+
			"/Temporaire/"+numero+".html' '"+destFichier+"'")
	
	elif platform.system() == "Windows":
		fichier = Codeur(self.ObjDoc.balises, self.ObjDoc.Doc.dump(0.0, END),
		self.ObjDoc.image)
		
		numero = str(int(time.time()))
		
		MecanismeConvHTML(fichier, CheminBeau(self.ObjDoc.cheminFichier),
		police=parPolice, auto=numero, arbo=parArbo)
	
		titre = re.sub(".* » ", "", CheminBeau(self.ObjDoc.cheminFichier))
	
		destFichier = asksaveasfilename(initialfile=titre+'.pdf',
		defaultextension='.pdf', filetypes=[('Fichier PDF','*.pdf')],
		initialdir=os.path.expanduser('~'), title='Exporter en PDF')

		if destFichier != "" and destFichier != None:	
			commande = '"'+os.environ['PROGRAMFILES']+\
			'\\wkhtmltopdf\\bin\wkhtmltopdf" "'+os.path.abspath('')+\
			'\\Temporaire\\'+numero+'.html" "'+destFichier+'"'

			commande.encode("utf8")
			subprocess.call(commande, shell=True)
