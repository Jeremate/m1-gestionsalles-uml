from patrimoine import batiment
from patrimoine import typesalle
from patrimoine import materiel
from patrimoine import typemateriel
from patrimoine import salle
from patrimoine import typesalle

#variables

class BatimentList(object):
	"""Classe représentant un ensemble de Batiment

	Attributs:

	"""
	
	def __init__(self):
		super(BatimentList, self).__init__()
		self.batiments = {}

	def __iter__(self):
		return self

	def __next__(self):
		for bat in self._batiments:
			return bat

	def __repr__(self):
		return repr(self.batiments)

	def ajouter_batiment(self,no_bat,nom,adresse):
		nouveau_bat = batiment.Batiment(no_bat,nom,adresse)
		if no_bat not in self.batiments:
			self.batiments[no_bat] = nouveau_bat

	def rechercher_batiment(self, no_bat):
		if no_bat in self.batiments:
			return self.batiments[no_bat]


	def modifier_batiment(self, no_bat, nom, adresse):
		if no_bat in self.batiments:
			nouveau_bat = batiment.Batiment(nom, adresse)
			batiments[no_bat] = nouveau_bat

	def supprimer_batiment(self, no_bat):
		if no_bat not in self.batiments:
			del self.batiments[no_bat]


class TypesalleList(object):
	"""Classe représentant un ensemble de typesalle

	Attributs:

	"""
	
	def __init__(self):
		super(TypesalleList, self).__init__()
		self.typesalles = {}

	def __iter__(self):
		return self

	def __next__(self):
		for ts in self._typesalles:
			return ts

	#fonctionnalitées typesalle
	def ajouter_typesalle(self, nom_typesalle, description):
		if nom_typesalle not in self.typesalles:
			nouveau_typesalle = typesalle.Typesalle(description)
			self.typesalles[nom_typesalle] = nouveau_typesalle

	def supprimer_typesalle(self, nom_typesalle):
		if nom_typesalle in self.typesalles:
			del self.typesalles[nom_typesalle]

	def consulter_typesalle(self, description):
		if nom_typesalle in self.typesalles:
			return self.typesalles[nom_typesalle]


class MaterielList(object):
	"""Classe représentant un ensemble de materiel

	Attributs:

	"""
	
	def __init__(self):
		super(MaterielList, self).__init__()
		self.materiels = {}

	def __iter__(self):
		return self

	def __next__(self):
		for materiel in self._materiels:
			return materiel

	#fonctionnalitées materiel
	def ajouter_materiel(self, code_inv):
		if code_inv not in self.materiels:
			nouveau_materiel = materiel.Materiel(code_inv)
			self.materiels[code_inv] = nouveau_materiel

	def supprimer_materiel(self, code_inv):
		if code_inv in self.materiels:
			del self.materiels[code_inv]

	def consulter_materiel(self, code_inv):
		if code_inv in self.materiels:
			return self.materiels[code_inv]
	#--------------------------------

class TypematerielList(object):
	"""Classe représentant un ensemble de typemateriel

	Attributs:

	"""
	
	def __init__(self):
		super(TypematerielList, self).__init__()
		self.typemateriels = {}

	def __iter__(self):
		return self

	def __next__(self):
		for tm in self._typemateriels:
			return tm

	#fonctionnalitées typemateriel
	def ajouter_typemateriel(self, nom):
		if nom not in self.typemateriels:
			nouveau_typemateriel = typemateriel.Typemateriel(nom)
			self.typemateriels[nom] = nouveau_typemateriel

	def supprimer_typemateriel(self, nom):
		if nom in self.typemateriels:
			del self.typemateriels[nom]

	def consulter_typemateriel(self, nom):
		if nom in self.typemateriels:
			return self.typemateriels[nom]


class SalleList(object):
	"""Classe représentant un ensemble de salle

	Attributs:

	"""
	
	def __init__(self):
		super(SalleList, self).__init__()
		self.salles = {}

	def __iter__(self):
		return self

	def __next__(self):
		for salle in self._salles:
			return salle


	#fonctionnalitées salle
	#fonction d'ajout d'une salle si le batiment ou le typesalle n'existe pas alors la fonction est abandonné
	def ajouter_salle(self,id_salle,no_etage,no_salle,no_bat,superficie,nom_typesalle):
		if id_salle not in self.salles:
			if no_bat in batiments:
				if nom_typesalle in typesalles:
					nouvelle_salle = salle.Salle(no_etage,no_salle,no_bat,superficie,typesalle)
					self.salles[id_salle] = nouvelle_salle

	#fonction pour supprimer une salle
	def supprimer_salle(self, id_salle):
		if id_salle in self.salles:
			for r in reservations:
				if r[id_salle].id_salle() == id_salle:
					del reservations[id_salle]
			del salles[id_salle]
	#-------------------------------

#fonctionnalitées pour la classe demandeur
def ajouter_demandeur(no_dem, nom):
	return 0


def main():

	batiments = BatimentList()
	batiments.ajouter_batiment(1,"Batiment 1","Adresse 1")
	batiments.supprimer_batiment(1)
	print (batiments.rechercher_batiment(1))

	print (batiments)

	"""ajouter_batiment(2,"bat_2","adresse_2")
	modifier_batiment(2,"bat_3","adresse_3")
	rechercher_batiment(2)"""
"""	ajouter_typemateriel("wow")
	supprimer_typemateriel("wow")
	ajouter_typesalle("classe")
	print(typesalles)
	#supprimer_typesalle()
	ajouter_salle(1,10,1,10,typesalles[0])"""
	#supprimer_salle(salles[0])
"""	print(typemateriels)
	print(batiments)
	print(salles)"""

if __name__ == '__main__':
	main()
