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

def Rien(toto=0):
	pass

def RaccourcisFormatage(self, fermer=False):
	# Raccourcis clavier

	if fermer == True:
		self.ObjDoc.Doc.bind("<Control-s>", Rien)
		self.ObjDoc.Doc.bind("<Control-S>", Rien)

		self.ObjDoc.Doc.bind("<Control-b>", Rien)
		self.ObjDoc.Doc.bind("<Control-B>", Rien)
		self.ObjDoc.Doc.bind("<Control-c>", Rien)
		self.ObjDoc.Doc.bind("<Control-C>", Rien)

		self.ObjDoc.Doc.bind("<Control-p>", Rien)
		self.ObjDoc.Doc.bind("<Control-P>", Rien)
		self.ObjDoc.Doc.bind("<Control-Shift-p>", Rien)
		self.ObjDoc.Doc.bind("<Control-Shift-P>", Rien)
		self.ObjDoc.Doc.bind("<Control-i>", Rien)
		self.ObjDoc.Doc.bind("<Control-I>", Rien)

		self.ObjDoc.Doc.bind("<Alt-a>", Rien)
		self.ObjDoc.Doc.bind("<Alt-A>", Rien)
		self.ObjDoc.Doc.bind("<Alt-z>", Rien)
		self.ObjDoc.Doc.bind("<Alt-Z>", Rien)
		self.ObjDoc.Doc.bind("<Alt-e>", Rien)
		self.ObjDoc.Doc.bind("<Alt-E>", Rien)
		self.ObjDoc.Doc.bind("<Alt-r>", Rien)
		self.ObjDoc.Doc.bind("<Alt-R>", Rien)

		self.ObjDoc.Doc.bind("<Control-e>", Rien)
		self.ObjDoc.Doc.bind("<Control-E>", Rien)

	else:
		self.ObjDoc.Doc.bind("<Control-s>", self.ObjDoc.Enr)
		self.ObjDoc.Doc.bind("<Control-S>", self.ObjDoc.Enr)

		self.ObjDoc.Doc.bind("<Control-b>", self.ObjDoc.Gras)
		self.ObjDoc.Doc.bind("<Control-B>", self.ObjDoc.Gras)
		self.ObjDoc.Doc.bind("<Control-c>", self.ObjDoc.Code)
		self.ObjDoc.Doc.bind("<Control-C>", self.ObjDoc.Code)

		self.ObjDoc.Doc.bind("<Control-p>", self.ObjDoc.Image)
		self.ObjDoc.Doc.bind("<Control-P>", self.ObjDoc.Image)
		self.ObjDoc.Doc.bind("<Control-Shift-p>", self.ObjDoc.ImageWeb)
		self.ObjDoc.Doc.bind("<Control-Shift-P>", self.ObjDoc.ImageWeb)
		self.ObjDoc.Doc.bind("<Control-i>", self.ObjDoc.CreerDessin)
		self.ObjDoc.Doc.bind("<Control-I>", self.ObjDoc.CreerDessin)

		self.ObjDoc.Doc.bind("<Alt-a>", self.ObjDoc.SurlignRien)
		self.ObjDoc.Doc.bind("<Alt-A>", self.ObjDoc.SurlignRien)
		self.ObjDoc.Doc.bind("<Alt-z>", self.ObjDoc.SurlignJaune)
		self.ObjDoc.Doc.bind("<Alt-Z>", self.ObjDoc.SurlignJaune)
		self.ObjDoc.Doc.bind("<Alt-e>", self.ObjDoc.SurlignVert)
		self.ObjDoc.Doc.bind("<Alt-E>", self.ObjDoc.SurlignVert)
		self.ObjDoc.Doc.bind("<Alt-r>", self.ObjDoc.SurlignBleu)
		self.ObjDoc.Doc.bind("<Alt-R>", self.ObjDoc.SurlignBleu)

		self.ObjDoc.Doc.bind("<Control-e>", self.ObjDoc.SupprFormatage)
		self.ObjDoc.Doc.bind("<Control-E>", self.ObjDoc.SupprFormatage)
