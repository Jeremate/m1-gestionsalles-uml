from patrimoine import batiment
from patrimoine import typesalle
from patrimoine import materiel
from patrimoine import typemateriel
from patrimoine import salle
from patrimoine import typesalle

#variables
#liste des batiment
batiments = {}
typesalles = []
materiels = []
typemateriels = []
salles = []

class BatimentList(object):
	"""Classe représentant un ensemble de Batiment

	Attributs:

	"""
	
	def __init__(self, arg):
		super(BatimentList, self).__init__()
		self._batiments = {}

	def __iter__(self):
		return self

	def __next__(self):
		for bat in self._batiments:
			return bat

	def ajouter_batiment(no_bat,nom,adresse):
		nouveau_bat = batiment.Batiment(no_bat,nom,adresse)
		if no_bat not in self.batiments:
			self.batiments[no_bat] = nouveau_bat
		
		

#fonctionnalitées batiment
def ajouter_batiment(no_bat,nom,adresse):
	nouveau_bat = batiment.Batiment(nom,adresse)
	if no_bat not in batiments:
		batiments[no_bat] = nouveau_bat


def rechercher_batiment(no_bat):
	print(no_bat," ",batiments[no_bat])


def modifier_batiment(no_bat,nom,adresse):
	nouveau_bat = batiment.Batiment(nom,adresse)
	if no_bat in batiments:
		batiments[no_bat] = nouveau_bat

def supprimer_batiment(no_bat):
	if no_bat not in batiments:
		del batiments[no_bat]

#fonctionnalitées typesalle
def ajouter_typesalle(nom):
	var_ajout = 1
	for ts in typesalles:
		if ts.nom == nom:
			var_ajout = 0
			break
	if var_ajout:
		nouveau_typesalle = typesalle.Typesalle(nom)
		typesalles.append(nouveau_typesalle)

def supprimer_typesalle(nom):
	for ts in typsalles:
		if ts.nom == nom:
			typesalle.remove(ts)

def consulter_typesalle(nom):
	for ts in typesalles:
		if ts.nom == nom:
			return ts
#fonctionnalitées materiel
def ajouter_materiel(code_inv):
	var_ajout = 1
	for m in materiels:
		if m.code_inv == code_inv:
			var_ajout = 0
			break
	if var_ajout:
		nouveau_materiel = materiel.Materiel(code_inv)
		materiels.append(nouveau_materiel)

def supprimer_materiel(code_inv):
	for m in materiels:
		if m.code_inv == code_inv:
			materiels.remove(m)
			break


#fonctionnalitées typemateriel
def ajouter_typemateriel(nom):
	var_ajout = 1
	for tm in typemateriels:
		if tm.nom == nom:
			var_ajout = 0
			break
	if var_ajout:
		nouveau_typemateriel = typemateriel.Typemateriel(nom)
		typemateriels.append(nouveau_typemateriel)

def supprimer_typemateriel(nom):
	for tm in typemateriels:
		if tm.nom == nom:
			"""typemateriels.remove(tm)
												break"""

def consulter_typemateriel(nom):
	for tm in typemateriels:
		if tm.nom == nom:
			return tm


#fonctionnalitées salle
#fonction d'ajout d'une salle si le batiment ou le typesalle n'existe pas alors la fonction est abandonné
def ajouter_salle(no_etage,no_salle,no_bat,superficie,typesalle):
	var_ajout = 0
	if no_bat in batiments:
		if typesalle in typesalles:
			var_ajout = 1
			for s in salles:
				if s.no_salle == no_salle and s.no_etage == no_etage:
					var_ajout = 0
					break
			if var_ajout:
				nouvelle_salle = salle.Salle(no_etage,no_salle,no_bat,superficie,typesalle)
				salles.append(nouvelle_salle)

#fonction pour supprimer une salle
def supprimer_salle(salle):
	if salle in salles:
		for r in reservations:
			if r.salle == salle:
				reservations.remove(r)
		salles.remove(salle)


#fonctionnalitées pour la classe demandeur



def main():
	batiments = BatimentList()
	ajouter_batiment(1,"bat_1","adresse_1")
	"""ajouter_batiment(2,"bat_2","adresse_2")
	modifier_batiment(2,"bat_3","adresse_3")
	rechercher_batiment(2)"""
	ajouter_typemateriel("wow")
	supprimer_typemateriel("wow")
	ajouter_typesalle("classe")
	print(typesalles)
	#supprimer_typesalle()
	ajouter_salle(1,10,1,10,typesalles[0])
	#supprimer_salle(salles[0])
	print(typemateriels)
	print(batiments)
	print(salles)

if __name__ == '__main__':
	main()
