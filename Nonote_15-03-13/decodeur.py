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

import re

def FichChercherImages(fichier):

	UrlImage = []
	varBoucle = fichier.count("<IMAGE>")

	i = 0
	while i < varBoucle:
		fichier = fichier.replace("<IMAGE>", "<IMAGE"+str(i)+">", 1)
		fichier = fichier.replace("</IMAGE>", "</IMAGE"+str(i)+">", 1)
		i += 1
	
	i = 0
	while i < varBoucle:
		element = re.sub("(.*)<IMAGE"+str(i)+">", "", fichier, flags=re.DOTALL)
		element = re.sub("</IMAGE"+str(i)+">(.*)", "", element, flags=re.DOTALL)
		UrlImage.append(element)
		i += 1
		
	return UrlImage

def FichChPositionsImages(fichier):

	fichier = fichier.replace("</IMAGE>", "")
	lignes = fichier.split("\n")

	i = 0
	liste = []

	while i < len(lignes):
		ii = 0
		nombreBalises = lignes[i].count("<IMAGE>")
		while ii < nombreBalises:
			liste.append(str(i+1)+"."+str(lignes[i].find("<IMAGE>")))
			lignes[i] = lignes[i].replace("<IMAGE>", "", 1)
			ii += 1
		i += 1

	return liste

def FichChPositions(balises, fichier, FORMAT):
	balisesDouble = []

	for a in balises:
		balisesDouble.append("/"+str(a))

	balises = balises + balisesDouble
	
	for b in balises:
		if FORMAT != b:
			fichier = fichier.replace("<"+b+">", "")
		
	lignes = fichier.split("\n")

	i = 0
	liste = []

	while i < len(lignes):
		ii = 0
		nombreBalises = lignes[i].count("<"+FORMAT+">")
		while ii < nombreBalises:
			liste.append(str(i+1)+"."+str(lignes[i].find("<"+FORMAT+">")))
			lignes[i] = lignes[i].replace("<"+FORMAT+">", "", 1)
			ii += 1
		i += 1

	return liste

def FichSupprBalises(balises, fichier, balise=""):

	for i in balises:
		if balise != i:
			fichier = fichier.replace("<"+i+">", "")
			fichier = fichier.replace("</"+i+">", "")
			
	fichier = re.sub("<IMAGE>(.*)</IMAGE>", "", fichier)
	fichier = fichier.replace("<LIEN>", "")
	fichier = fichier.replace("</LIEN>", "")
		
	return fichier
