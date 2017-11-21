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

import platform, os, time
from decodeur import *
from codeur import *
from tkinter import *
from PIL import Image, ImageTk

def CheminBeau(chemin):
    CheminBeau = chemin.replace('\\', ' » ')
    CheminBeau = CheminBeau.replace('/', ' » ')
    CheminBeau = CheminBeau.replace('.nonote', '')
    return CheminBeau

def c(chemin):
	if platform.system() == "Windows":
		chemin = chemin.replace('/', '\\')
	return chemin

def s():
	if platform.system() == "Windows":
		return "\\"
	else:
		return "/"
		
def ImgSupprimer(fichier):
	listeSuppr = FichChercherImages(fichier)
	if listeSuppr != []:
		for i in listeSuppr:
			try:
				os.remove("./Images/"+i)
			except:
				pass

def ImgSupprInutile(images, fichier):
	listeAjoute = []
	for i in images:
		listeAjoute.append(str(i))

	listeSuppr = []
	listeActuelle = FichChercherImages(fichier)
	
	for i in listeAjoute:
		if i not in listeActuelle:
			listeSuppr.append(i)
			
	if listeSuppr != []:
		for i in listeSuppr:
			try:
				os.remove("./Images/"+i)
			except:
				pass

def EcranChargement(self):
	self.fenetre.withdraw()
	self.splash = Toplevel()

	scrnWt = self.splash.winfo_screenwidth()
	scrnHt = self.splash.winfo_screenheight()
	
	self.image = ImageTk.PhotoImage(Image.open('Icones/demarrage.png'))

	imgWt = self.image.width()
	imgHt = self.image.height()

	imgXPos = (scrnWt / 2) - (imgWt / 2)
	imgYPos = (scrnHt / 2) - (imgHt / 2)

	self.splash.overrideredirect(1)
	self.splash.geometry( '+%d+%d' % (imgXPos, imgYPos) )

	imageChargement = Label(self.splash, image=self.image,
	cursor='watch').pack()

	self.splash.update()

def FermerChargement(self):
	self.splash.destroy( )
	self.fenetre.deiconify()
