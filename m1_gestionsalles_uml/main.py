from patrimoine import batiment
from patrimoine import typesalle
from patrimoine import materiel
from patrimoine import typemateriel
from patrimoine import salle
from patrimoine import typesalle

#variables
batiments = {}
typesalles = {}
materiels = {}
typemateriels = {}
salles = {}
reservations = {}

#fonctionnalitées batiment
def ajouter_batiment(no_bat, nom, adresse):
	if no_bat not in batiments:
		nouveau_bat = batiment.Batiment(no_bat, nom, adresse)
		batiments[no_bat] = nouveau_bat


def rechercher_batiment(no_bat):
	if no_bat in batiments:
		return batiments[no_bat]


def modifier_batiment(no_bat,nom,adresse):
	if no_bat in batiments:
		nouveau_bat = batiment.Batiment(nom,adresse)
		batiments[no_bat] = nouveau_bat

def supprimer_batiment(no_bat):
	if no_bat not in batiments:
		del batiments[no_bat]
#----------------------------


#fonctionnalitées typesalle
def ajouter_typesalle(nom_typesalle,description):
	if nom_typesalle not in typesalles:
		nouveau_typesalle = typesalle.Typesalle(description)
		typesalles[nom_typesalle] = nouveau_typesalle

def supprimer_typesalle(nom_typesalle):
	if nom_typesalle in typesalles:
		del typesalles[nom_typesalle]

def consulter_typesalle(description):
	if nom_typesalle in typesalles:
		return typesalles[nom_typesalle]

#fonctionnalitées materiel
def ajouter_materiel(code_inv):
	if code_inv not in materiels:
		nouveau_materiel = materiel.Materiel(code_inv)
		materiels[code_inv] = nouveau_materiel

def supprimer_materiel(code_inv):
	if code_inv in materiels:
		del materiels[code_inv]

def consulter_materiel(code_inv):
	if code_inv in materiels:
		return materiels[code_inv]
#--------------------------------

#fonctionnalitées typemateriel
def ajouter_typemateriel(nom):
	if nom not in typemateriels:
		nouveau_typemateriel = typemateriel.Typemateriel(nom)
		typemateriels[nom] = nouveau_typemateriel

def supprimer_typemateriel(nom):
	if nom in typemateriels:
		del typemateriels[nom]

def consulter_typemateriel(nom):
	if nom in typemateriels:
		return typemateriels[nom]


#fonctionnalitées salle
#fonction d'ajout d'une salle si le batiment ou le typesalle n'existe pas alors la fonction est abandonné
def ajouter_salle(id_salle,no_etage,no_salle,no_bat,superficie,nom_typesalle):
	if id_salle not in salles:
		if no_bat in batiments:
			if nom_typesalle in typesalles:
				nouvelle_salle = salle.Salle(no_etage,no_salle,no_bat,superficie,typesalle)
				salles[id_salle] = nouvelle_salle

#fonction pour supprimer une salle
def supprimer_salle(id_salle):
	if id_salle in salles:
		for r in reservations:
			if r[id_salle].id_salle() == id_salle:
				del reservations[id_salle]
		del salles[id_salle]
#-------------------------------

#fonctionnalitées pour la classe demandeur
def ajouter_demandeur(no_dem, nom):
	return 0


def main():

	print (typesalles)
	print(typemateriels)
	print(batiments)
	print(salles)

if __name__ == '__main__':
	main()
