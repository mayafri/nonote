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
import platform

def Centrage(fenetre):
	w = fenetre.winfo_screenwidth()
	h = fenetre.winfo_screenheight()
	rootsize = fenetre.geometry().split('+')[0].split('x')
	print(geo, rootsize)
	x = w/2 - int(rootsize[0])/2
	x = str(x)
	x = x.split('.')
	y = h/2 - int(rootsize[1])/2
	y = str(y)
	y = y.split('.')
	fenetre.geometry("+"+x[0]+"+"+y[0])

def Licence():
	FLicence = Toplevel()
	FLicence.grab_set()

	if platform.system() == "Windows":
		FLicence.iconbitmap('Icones\logo.ico')

	FLicence.title("Licence")
	FLicence.resizable(False,False)
	
	fichierLicence = open("Special/licence.txt", 'r', encoding='utf-8')
	varFichierLicence = fichierLicence.read()
	fichierLicence.close()
	
	cadre = ScrolledText(FLicence)
	cadre.insert("0.0", varFichierLicence)
	cadre.config(highlightthickness=0, wrap='word', width=80, height=25)
	cadre.pack()
	
	boutonFermer = ttk.Button(FLicence, text="Fermer", command=FLicence.destroy)
	boutonFermer.pack(padx=6, pady=6)
	
def Credits():
	FCredits = Toplevel()
	FCredits.grab_set()

	if platform.system() == "Windows":
		FCredits.iconbitmap('Icones\logo.ico')

	FCredits.title("Crédits")
	FCredits.resizable(False,False)
	
	cadre = Label(FCredits, text="\
Je remercie mon frère Cyril\n\
qui m'a donné la motivation\n\
de m'amuser avec Python ainsi\n\
que de m'occuper de ce projet.\n\n\
Réalisé par Maya Friedrichs.").pack(padx=6, pady=6)
	
	boutonFermer = ttk.Button(FCredits, text="Fermer", command=FCredits.destroy)
	boutonFermer.pack(padx=6, pady=6)

def APropos(self):
	if platform.system() == "Windows":
		self.bandeau = PhotoImage(file="Icones\\apropos win.gif")
	elif platform.system() == "Darwin":
		self.bandeau = PhotoImage(file="Icones/apropos mac.gif")
	else:
		self.bandeau = PhotoImage(file="Icones/apropos blanc.gif")

	FAPropos = Toplevel()
	FAPropos.grab_set()

	if platform.system() == "Windows":
		FAPropos.iconbitmap('Icones\logo.ico')

	FAPropos.title("À propos")
	FAPropos.resizable(False,False)

	labelImage = Label(FAPropos, image=self.bandeau)
	
	labelTexte = Label(FAPropos, text="Version de développement 15-03-13")
	labelTexte.config(pady="10")

	boutonLicence = ttk.Button(FAPropos, text="Licence", command=Licence)
	boutonCredits = ttk.Button(FAPropos, text="Crédits", command=Credits)
	boutonFermer = ttk.Button(FAPropos, text="Fermer", command=FAPropos.destroy)

	labelImage.grid(row=0, column=0, columnspan=3)
	labelTexte.grid(row=1, column=0, columnspan=3)
	boutonLicence.grid(row=2, column=0, padx=6, pady=6)
	boutonCredits.grid(row=2, column=1, padx=6, pady=6)
	boutonFermer.grid(row=2, column=2, padx=6, pady=6)

