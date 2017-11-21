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

import re, os, shutil
from tkinter import *
from tkinter.filedialog import asksaveasfilename

# Fenêtre d'options

def ConvTXT(fichier, CheminBeau, balises):
	varArborescence = IntVar()
	varTitre = IntVar()

	def Convertir():
		MecanismeConvTXT(fichier, CheminBeau, balises, varArborescence.get(),
		varTitre.get())
		OptionsTXT.destroy()
	
	OptionsTXT = Toplevel()
	OptionsTXT.grab_set()
	OptionsTXT.title("Exporter en texte simple")
	OptionsTXT.resizable(False,False)
		
	label = Label(OptionsTXT, text="Attention, la mise en forme\n\
ne sera pas conservée.")

	checkTitre = Checkbutton(OptionsTXT, text="Insérer le titre",
	variable=varTitre)

	checkArbo = Checkbutton(OptionsTXT, text="Insérer l'arborescence",
	variable=varArborescence)
	
	boutonAnnuler = ttk.Button(OptionsTXT, text="Annuler",
	command=OptionsTXT.destroy)
	boutonOK = ttk.Button(OptionsTXT, text="Exporter", command=Convertir)

	checkTitre.grid(row=0, column=0, columnspan=2, padx="5", pady="2",
	sticky="W")
	checkArbo.grid(row=1, column=0, columnspan=2, padx="5", pady="2",
	sticky="W")
	label.grid(row=2, column=0, columnspan=2, padx="5", pady="2")
	boutonAnnuler.grid(row=3, column=0, padx="5", pady="2")
	boutonOK.grid(row=3, column=1, padx="5", pady="2")
	

def MecanismeConvTXT(fichier, CheminBeau, balises, boolArbo=0, boolTitre=0):

	# Suppression des balises

	fichier = fichier.replace("<T4>", "# ")
	fichier = fichier.replace("<T4>", " ")
	fichier = fichier.replace("<T3>", "## ")
	fichier = fichier.replace("<T3>", " ")
	fichier = fichier.replace("<T2>", "### ")
	fichier = fichier.replace("<T2>", " ")
	fichier = fichier.replace("<T1>", "#### ")
	fichier = fichier.replace("<T1>", "")
	for i in balises:
		fichier = fichier.replace("</"+i+">", "")
		fichier = fichier.replace("<"+i+">", "")
	fichier = re.sub("<IMAGE>(.*)</IMAGE>", "", fichier)

	# Rajout des options choisies

	titre = re.sub(".* » ", "", CheminBeau)

	if boolTitre == 1:
		i = 0
		souligne = ""
		
		while i < len(titre):
			souligne = souligne+"="
			i += 1
		
		fichier = re.sub("^",souligne+"\n\n", str(fichier))
		fichier = re.sub("^", titre.upper()+"\n", str(fichier))

	if boolArbo == 1:
		fichier = re.sub("^", "["+CheminBeau+"]\n\n", str(fichier))

	# Choix de l'emplacement et du nom

	destFichier = asksaveasfilename(initialfile=titre+'.txt',
	defaultextension='.txt', filetypes=[('Fichier TXT','*.txt')],
	initialdir=os.path.expanduser('~'), title='Exporter en texte simple')

	destFichierSansExt = destFichier.rsplit(".", 1)
	FichierSansExt = destFichierSansExt[0].rsplit("/", -1)

	#Enregistrement

	if destFichier != "" and destFichier != None:
		file = open(destFichier, 'w+', encoding='utf-8')
		file.write(fichier)
		file.close

