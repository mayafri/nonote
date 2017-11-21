# Nonote : prendre et organiser des notes

![](https://raw.githubusercontent.com/hyakosm/nonote/master/nonote.png)

**Je ne m'occupe aujourd'hui plus de Nonote ni de rien codé en Tkinter. Ce projet date du temps où je ne pratiquais pas encore l'orienté objet.**

Nonote est une application multiplateforme pour prendre des notes sous forme de texte formaté, y ajouter des éléments, et pour pouvoir les organiser directement en utilisant des dossiers qui peuvent être imbriqués. Le contenu peut être exporté en texte brut, en page HTML ou en document PDF. Nonote est conçu pour écrire du contenu de façon élégante rapidement. Les options de formatage sont peu nombreuses et la gestion des dossiers est intégrée, pour se concentrer sur son travail et être le plus efficace possible.

Nonote est mis à disposition sous licence CeCILL (compatible GPL, mais rédigée pour le droit français).

![](https://raw.githubusercontent.com/hyakosm/nonote/master/nonote1.png)

![](https://raw.githubusercontent.com/hyakosm/nonote/master/nonote2.png)

![](https://raw.githubusercontent.com/hyakosm/nonote/master/nonote3.png)

![](https://raw.githubusercontent.com/hyakosm/nonote/master/nonote4.png)

![](https://raw.githubusercontent.com/hyakosm/nonote/master/nonote5.png)

## Fonctionnalités

### Actuellement :

    Classement des pages dans des dossiers hiérarchisés
    Texte formaté (gras, chasse fixe, trois surlignages)
    Styles (paragraphe, 4 niveaux de titres, citation, source, avertissement conseil)
    Liens hypertexte (un clic dessus, et le navigateur s'ouvre à la bonne page)
    Insertion d'images en local ou depuis une URL
    Dessin depuis Paint ou XPaint
    Export en texte brut, HTML ou PDF
    Interface personnalisable (couleur de fond, police et taille de caractère)

### Pour la prochaine version stable :

    Correction de bogues
    Optimisation du code
    Guide d'utilisation
    Fonction de recherche dans le fichier, ou à travers les fichiers
    Synchronisation sur un serveur personnel
    Gestion d'OS X
    Tableau blanc, pour dessiner sans passer par Paint ou XPaint
    Tableaux de texte
    Gestion des images plus agréable et plus complète
    Éléments Web

## Prérequis

### Obligatoires :

    Python 3 (paquet python3 sur ma Debian)
    PIL pour Python 3 (paquet python3-pil sur ma Debian)
    Tkinter pour Python 3 (déjà intégré dans la paquet Windows, paquet python3-tk sur ma Debian)
    ImageTk pour Python 3 (déjà intégré dans la paquet Windows, paquet python3-pil.imagetk sur ma Debian)

### Optionnels :

    WkHTMLtoPDF pour exporter les notes en PDF (paquet wkhtmltopdf sur ma Debian)
    XPaint (GNU/Linux uniquement) pour dessiner (paquet xpaint sur ma Debian)

Sur Windows, il est important de récupérer les paquets correspondant à son architecture (32 ou 64 bits).

## Téléchargement

L'archive est disponible ici.

Attention, Nonote comporte beaucoup de bogues et certaines fonctionnalités ne sont pas finies, on peut le considérer comme une version alpha.

## Lancement

### Avec GNU/Linux

On peut le lancer depuis la console facilement :

`python3 "/chemin/chemin/chemin/Nonote.pyw"`

On peut lancer le script avec interface graphique en double-cliquant dessus, si l'association des fichiers de type .pyw a été définie avec python3.

Il est aussi possible d'utiliser un script bash pour créer l'équivalent d'un lien, sans toucher aux associations de fichier, ce qui est utile pour garder les fichiers Python associés à l'éditeur par exemple :

`#!/bin/sh`
`python3 "/chemin/chemin/chemin/Nonote.pyw"`

### Avec MS Windows

On peut lancer Nonote en double-cliquant sur Nonote.pyw.

Pour le lancer en gardant le retour de la console Python, il suffit de cliquer sur Nonote avec console.bat.
Quelques mots sur les notes

Nonote encode en interne les fichiers au format .nonote, il s'agit en réalité de simple fichiers de texte brut, qui contiennent un langage de balise très simple semblable au HTML, mais adapté aux fonctionnalités de Nonote. Ce langage n'est certes pas standard mais il est ouvert. On peut éditer librement n'importe lequel de ces fichiers. Pour exporter une note, il est toutefois conseillé d'utiliser les fonctions d'export (mais tu peux coder ton propre parseur si tu veux).

Les notes sont réellement classées dans de vrais dossiers sur le disque. Ainsi, quand on crée un dossier sur Nonote, il est créé sur le disque. Ceci est parfaitement standard.
