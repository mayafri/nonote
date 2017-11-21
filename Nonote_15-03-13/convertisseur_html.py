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

import re, os, shutil, webbrowser, tkinter.font
from tkinter import *
from tkinter.filedialog import asksaveasfilename

# Fenêtre d'options

def ConvHTML(fichier, CheminBeau, auto=""):
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

		MecanismeConvHTML(fichier, CheminBeau, police=policeGet(),
		arbo=varArborescence.get(), auto=nomAuto)
		if nomAuto=="":
			OptionsHTML.destroy()

	def Apercu():
		Convertir(nomAuto="apercu")
		webbrowser.open_new("file://"+os.path.dirname(__file__)+"/Temporaire/apercu.html/")
	
	OptionsHTML = Toplevel()
	OptionsHTML.grab_set()
	OptionsHTML.title("Exporter en HTML")
	OptionsHTML.resizable(False,False)
		
	checkArbo = Checkbutton(OptionsHTML, text="Insérer l'arborescence",
	variable=varArborescence)

	def PoliceCheckWidget():
		if varPolice.get() == 2:
			choixPolice.configure(state='readonly')
			label.grid(row=4, column=0, columnspan=3, padx="5", pady="2")
		else:
			choixPolice.configure(state='disabled')
			label.grid_forget()

	choixPoliceListe = list(font.families())

	radio1 = ttk.Radiobutton(OptionsHTML, text="Police Serif \
(de type Serif Times)",
	variable=varPolice, value=0, command=PoliceCheckWidget)
	
	radio2 = ttk.Radiobutton(OptionsHTML, text="Police Sans-Serif \
(de type Helvetica ou Arial)",
	variable=varPolice, value=1, command=PoliceCheckWidget)
	
	radio3 = ttk.Radiobutton(OptionsHTML, text="Police personnalisée",
	variable=varPolice, value=2, command=PoliceCheckWidget)	

	choixPolice = ttk.Combobox(OptionsHTML,
	values=choixPoliceListe, state='disabled')

	label = Label(OptionsHTML, text="Attention, si vous publiez ce fichier, \
les autres utilisateurs\ndevront avoir la même police de caractère installée.")
	
	boutonAnnuler = ttk.Button(OptionsHTML, text="Annuler",
	command=OptionsHTML.destroy)
	boutonApercu = ttk.Button(OptionsHTML, text="Aperçu", command=Apercu)
	boutonOK = ttk.Button(OptionsHTML, text="Exporter", command=Convertir)

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
	

def MecanismeConvHTML(fichier, CheminBeau, police, auto="", arbo=1):

	titre = re.sub(".* » ", "", CheminBeau)

	fichier = fichier.replace("<", "&lt;")
	fichier = fichier.replace(">", "&gt;")
	
	fichier = fichier.replace("\n\n", "</p><p>")
	fichier = fichier.replace("\n", "<br />")
	fichier = fichier.replace("</p><p>", "</p>\n<p>")

	fichier = fichier.replace("  ", "&emsp;&emsp;")
	fichier = fichier.replace("\n</", "</")

	if police == "serif" or police == "sans-serif":
		policeDefaut = police
	else:
		policeDefaut = "\""+police+"\", serif"
	policeDefautMono = "monospace, courier"

	fichier = re.sub("^", "<h1>"+titre+"</h1>\n<p>", str(fichier))

	if arbo == 1:
		fichier = re.sub("^", "<p id='parcours'>"+CheminBeau+"</p>\n",
		str(fichier))

	fichier = re.sub("^", "\
<html>\n\
	<head>\n\
	    <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />\n\
		<title>"+titre+"</title>\n\
		<style type='text/css'>\n\
			body { font-family: "+policeDefaut+" }\n\
			.code { font-family: "+policeDefautMono+" }\n\
			#parcours { font-style: italic; color: gray }\n\
			.jaune { background-color: yellow }\n\
			.vert { background-color: lime }\n\
			.bleu { background-color: aqua }\n\
			.t1 { font-size: 2.5em }\n\
			.t2 { font-size: 2em }\n\
			.t3 { font-size: 1.8em }\n\
			.t4 { font-size: 1.3em }\n\
			.avertissement {\
margin-left: 2em; color: #ea0000; font-weight: bold }\n\
			.conseil { margin-left: 2em; color: #007f7f; font-weight: bold }\n\
			.auteur { margin-left: 5em; font-size: 0.8em }\n\
			quote { margin-left: 2em; font-style: italic }\n\
		</style>\n\
	</head>\n\
	<body>\n", str(fichier))

	fichier = re.sub("$", "</p>\n</body>\n</html>", str(fichier))	

	fichier = fichier.replace("&lt;GRAS&gt;", "<strong>")
	fichier = fichier.replace("&lt;JAUNE&gt;", "<span class='jaune'>")
	fichier = fichier.replace("&lt;VERT&gt;", "<span class='vert'>")
	fichier = fichier.replace("&lt;BLEU&gt;", "<span class='bleu'>")
	fichier = fichier.replace("&lt;T1&gt;", "<span class='t1'>")
	fichier = fichier.replace("&lt;T2&gt;", "<span class='t2'>")
	fichier = fichier.replace("&lt;T3&gt;", "<span class='t3'>")
	fichier = fichier.replace("&lt;T4&gt;", "<span class='t4'>")
	fichier = fichier.replace("&lt;CITATION&gt;", "\n<quote>")
	fichier = fichier.replace("&lt;AVERTISSEMENT&gt;",
	"\n<span class='avertissement'>")
	fichier = fichier.replace("&lt;CONSEIL&gt;", "\n<span class='conseil'>")
	fichier = fichier.replace("&lt;AUTEUR&gt;", "\n<span class='auteur'>")
	fichier = fichier.replace("&lt;CODE&gt;", "\n<span class='code'>")
	
	fichier = fichier.replace("&lt;/GRAS&gt;", "</strong>")
	fichier = fichier.replace("&lt;/JAUNE&gt;", "</span>")
	fichier = fichier.replace("&lt;/VERT&gt;", "</span>")
	fichier = fichier.replace("&lt;/BLEU&gt;", "</span>")
	fichier = fichier.replace("&lt;/T1&gt;", "</span>\n")
	fichier = fichier.replace("&lt;/T2&gt;", "</span>\n")
	fichier = fichier.replace("&lt;/T3&gt;", "</span>\n")
	fichier = fichier.replace("&lt;/T4&gt;", "</span>\n")
	fichier = fichier.replace("&lt;/CITATION&gt;", "</quote>\n")
	fichier = fichier.replace("&lt;/AVERTISSEMENT&gt;", "</span>\n")
	fichier = fichier.replace("&lt;/CONSEIL&gt;", "</span>\n")
	fichier = fichier.replace("&lt;/AUTEUR&gt;", "</span>\n")
	fichier = fichier.replace("&lt;/CODE&gt;", "</span>")

	fichier = fichier.replace("&lt;LIEN&gt;", "<a href=\"")
	fichier = fichier.replace("&lt;/LIEN&gt;", "\">[LIEN]</a>")
	
	# Gestion des images
	
	varBoucle = fichier.count("&lt;IMAGE&gt;")

	i = 0
	while i < varBoucle:
		fichier = fichier.replace("&lt;IMAGE&gt;", "<IMAGE"+str(i)+">", 1)
		fichier = fichier.replace("&lt;/IMAGE&gt;", "</IMAGE"+str(i)+">", 1)
		i += 1
	
	UrlImage = []
	i = 0
	while i < varBoucle:
		element = re.sub("(.*)<IMAGE"+str(i)+">", "", fichier, flags=re.DOTALL)
		element = re.sub("</IMAGE"+str(i)+">(.*)", "", element, flags=re.DOTALL)
		UrlImage.append(element)
		i += 1

	# Choix de l'emplacement et du nom

	if auto == "":
		destFichier = asksaveasfilename(initialfile=titre+'.html',
		defaultextension='.html', filetypes=[('Fichier HTML','*.html')],
		initialdir=os.path.expanduser('~'), title='Exporter en HTML')
	else:
		destFichier = "Temporaire/"+auto+".html"

	destFichierSansExt = destFichier.rsplit(".", 1)
	FichierSansExt = destFichierSansExt[0].rsplit("/", -1)
	
	# Personnalisation du chemin des images en fonction du nom choisi
	
	i = 0
	while i < varBoucle:
		fichier = re.sub("<IMAGE[0-9]*>",
		"<img src='"+FichierSansExt[-1]+"_images/", fichier)
		fichier = re.sub("</IMAGE[0-9]*>", "' alt='' />", fichier)
		i += 1

	#Enregistrement

	if destFichier != "" and destFichier != None:
		file = open(destFichier, 'w+', encoding='utf-8')
		file.write(fichier)
		file.close
				
		if UrlImage != []:
			os.mkdir(destFichierSansExt[0]+"_images")
			for i in UrlImage:
				shutil.copyfile("./Images/"+i,
				destFichierSansExt[0]+"_images/"+i)

