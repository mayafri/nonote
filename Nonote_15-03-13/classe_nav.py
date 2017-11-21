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

import os, shutil, re
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox

from classe_nav_int import *
from utilitaire import *

class ClasseNav(ClasseNavInt):
	def __init__(self):
			ClasseNavInt.__init__(self)
			self.dosNouv.configure(command=self.DCreer)
			self.dosSuppr.configure(command=self.DSuppr)
			self.dosRm.configure(command=self.DRm)
			self.dosDeplacer.configure(command=self.DDepl)

			self.fichNouv.configure(command=self.FCreer)
			self.fichSuppr.configure(command=self.FSuppr)
			self.fichRm.configure(command=self.FRm)
			self.fichDeplacer.configure(command=self.FDepl)

	def DCreer(self): 
		question = simpledialog.askstring('Nouveau classeur',
		'Nom voulu pour le classeur :')
		
		if question != "" and question != None:
		
			if os.path.isdir(self.focusDossiers+s()+question) == True or\
			os.path.isfile(self.focusDossiers+s()+question) == True:
			
				messagebox.showerror(message='Ce nom est déjà utilisé.')
			else:
				os.mkdir(self.focusDossiers+s()+question)
				self.AfficherDossiers()

	def FCreer(self): 
		question = simpledialog.askstring('Nouveau document',
		'Nom voulu pour le document :')
		
		if question != "" and question != None:
		
			if os.path.isdir(self.focusDossiers+s()+question) == True or\
			os.path.isfile(self.focusDossiers+s()+question) == True:
			
				messagebox.showerror(message='Ce nom est déjà utilisé.')
			else:
				fichier = open(self.focusDossiers+s()+question+".nonote", "w")
				self.AfficherFichiers()
				
	def DSuppr(self):	
		if self.focusDossiers != self.racine:
			if self.cheminFichier.find(self.focusDossiers) == -1 :
			
				question = messagebox.askyesno(
				message="Voulez-vous supprimer le classeur "+
				self.focusDossiers+" ?",
				icon='question', title="Supprimer le classeur")
				
				if question == True:
					listeFichiers = []
					
					for subdir, dirs, files in os.walk(self.focusDossiers):
						for file in files:
							listeFichiers.append(os.path.join(subdir, file))
				
					for i in listeFichiers:
						if os.path.isfile(i):
							fichier = open(i)
							ImgSupprimer(fichier.read())
							fichier.close()
				
					shutil.rmtree(self.focusDossiers)
					self.AfficherDossiers()
			else:
				messagebox.showinfo("Suppression impossible",
				"Vous devez fermer le document ouvert dans ce dossier.")

	def FSuppr(self):
		if self.focusFichiers != "":
			if self.cheminFichier != self.focusFichiers:
			
				question = messagebox.askyesno(
				message="Voulez-vous supprimer le document "+
				self.focusFichiers+" ?",
				icon='question', title="Supprimer le document")
				
				if question == True:
					fichier = open(self.focusFichiers)
					ImgSupprimer(fichier.read())
					fichier.close()
					os.remove(self.focusFichiers)
					self.AfficherFichiers()
			else:
				messagebox.showinfo("Suppression impossible",
				"Vous devez fermer le document ouvert.")
				
	def DRm(self):
		if self.focusDossiers != self.racine:
			if self.cheminFichier.find(self.focusDossiers) == -1 :
				question = simpledialog.askstring('Renommer le classeur',
				'Nouveau nom pour le classeur :')
				
				if question != "" and question != None:
					if os.path.isdir(os.path.dirname(self.focusDossiers)+
					s()+question) == True or\
					os.path.isfile(os.path.dirname(self.focusDossiers)
					+s()+question) == True:
					
						messagebox.showerror(message='Ce nom est déjà utilisé.')
					else:
						os.rename(self.focusDossiers,
						os.path.dirname(self.focusDossiers)+s()+question)
						
						self.AfficherDossiers()
			else:
				messagebox.showinfo("Renommage impossible",
				"Vous devez fermer le document ouvert dans ce dossier.")

	def FRm(self):
		if self.focusFichiers != "":
			if self.cheminFichier != self.focusFichiers:
				question = simpledialog.askstring('Renommer le document',
				'Nouveau nom pour le document :')
				
				if question != "" and question != None:
					if os.path.isdir(os.path.dirname(self.focusDossiers)+
					s()+question) == True or\
					os.path.isfile(os.path.dirname(self.focusDossiers)+
					s()+question) == True:
					
						messagebox.showerror(message='Ce nom est déjà utilisé.')
					else:
						os.rename(self.focusFichiers, self.focusDossiers+
						s()+question+".nonote")
						
						self.AfficherFichiers()
			else:
				messagebox.showinfo("Renommage impossible",
				"Vous devez fermer le document ouvert.")

	def DDepl(self):
		if self.focusDossiers != self.racine:
			if self.cheminFichier.find(self.focusDossiers) == -1 :
				fenetreD = Toplevel()
				fenetreD.grab_set()
				fenetreD.title("Déplacer le classeur")	

				def OK():
					nouveauChemin = ExploDos.focus()+s()+\
					os.path.basename(self.focusDossiers)
					
					if os.path.isfile(nouveauChemin) == True or\
					os.path.isdir(nouveauChemin) == True:
						messagebox.showerror(message=
						'Un élément du même nom existe déjà à cet endroit.')
					else:
						shutil.move(self.focusDossiers, ExploDos.focus())
						fenetreD.destroy()
						self.AfficherDossiers()

				fenetreD.resizable(False,False)

				message = Label(fenetreD, text=
				"Où souhaitez-vous\nmettre le classeur ?")

				frameA = Frame(fenetreD)

				scroll = ttk.Scrollbar(frameA)
				
				ExploDos = ttk.Treeview(frameA, yscrollcommand=scroll.set,
				selectmode="browse", show="tree")
				
				ExploDos.insert("", 0, self.racine, text=self.racine)
				
				ExploDos.item(self.racine, open=True)
				
				scroll.config(command=ExploDos.yview)
				
				for root, dirs, files in os.walk(self.racine):     
					for i in dirs:
						ExploDos.insert(root, 0, root+s()+i, text=i)
				ExploDos.delete(self.focusDossiers)

				ExploDos.pack(side=LEFT)
				scroll.pack(side=LEFT, fill=Y)
				
				frameB = Frame(fenetreD)
				
				boutonAnnuler = ttk.Button(frameB, text="Annuler",
				command=fenetreD.destroy)
				boutonOK = ttk.Button(frameB, text="OK", command=OK)
				
				boutonAnnuler.pack(side=RIGHT)
				boutonOK.pack(side=RIGHT, padx=6)

				message.grid(row=0, column=0, sticky=NSEW, padx=6, pady=6)
				frameA.grid(row=1, column=0, sticky=NSEW, padx=6)
				frameB.grid(row=2, column=0, sticky=NSEW, padx=6, pady=6)
			else:
				messagebox.showinfo("Déplacement impossible",
				"Vous devez fermer le document ouvert dans ce dossier.")

	def FDepl(self):
		if self.focusFichiers != "":
			if self.cheminFichier != self.focusFichiers:
				fenetreF = Toplevel()
				fenetreF.grab_set()		
				fenetreF.title("Déplacer le document")	

				def OK():
					nouveauChemin = ExploFich.focus()+s()+\
					os.path.basename(self.focusFichiers)
					
					if os.path.isfile(nouveauChemin) == True or\
					os.path.isdir(nouveauChemin) == True:
						messagebox.showerror(message=
						'Un élément du même nom existe déjà à cet endroit.')
					else:
						shutil.move(self.focusFichiers, ExploFich.focus())
						fenetreF.destroy()
						self.AfficherFichiers()

				fenetreF.resizable(False,False)

				message = Label(fenetreF, text=
				"Où souhaitez-vous\nmettre le document ?")

				frameA = Frame(fenetreF)

				scroll = ttk.Scrollbar(frameA)
				
				ExploFich = ttk.Treeview(frameA, yscrollcommand=scroll.set,
				selectmode="browse", show="tree")
				
				ExploFich.insert("", 0, self.racine, text=self.racine)
				
				ExploFich.item(self.racine, open=True)
				
				scroll.config(command=ExploFich.yview)
			
				for root, dirs, files in os.walk(self.racine):     
					for i in dirs:
						ExploFich.insert(root, 0, root+s()+i, text=i)

				ExploFich.pack(side=LEFT)
				scroll.pack(side=LEFT, fill=Y)

				frameB = Frame(fenetreF)
				
				boutonAnnuler = ttk.Button(frameB, text="Annuler",
				command=fenetreF.destroy)
				boutonOK = ttk.Button(frameB, text="OK", command=OK)
				
				boutonAnnuler.pack(side=RIGHT)
				boutonOK.pack(side=RIGHT, padx=6)

				message.grid(row=0, column=0, sticky=NSEW, padx=6, pady=6)
				frameA.grid(row=1, column=0, sticky=NSEW, padx=6)
				frameB.grid(row=2, column=0, sticky=NSEW, padx=6, pady=6)
			else:
				messagebox.showinfo("Déplacement impossible",
				"Vous devez fermer le document ouvert.")
