from patrimoine import batiment
from patrimoine import typesalle
from patrimoine import materiel
from patrimoine import typemateriel
from patrimoine import salle
from patrimoine import typesalle
from finance.tabletarif import TableTarif
from localisation.adresse import Adresse

#variables

class GestionAPI(object):
	"""Classe représentant le systeme de gestion de salle

	Attributs:

	"""
	
	def __init__(self):
		super(GestionAPI, self).__init__()
		self._batiments = {}
		self._materiels = {}
		self._typemateriels = {}
		self._typesalles = {}
		self._demandeur = {}
		self._reservations = {}
		self._origine = {}
		self._durer = {}
		self._manifestation = {}
		self._adresses = {}



	def adresses(self):
		return self._adresses

	def ajouter_adresse(id_adresse, no, adresse, code, ville):
		if id_adresse not in self._adresses:
			self._adresses[id_adresse] = Adresse(no, adresse, code, ville)

	def supprimer_adresse(id_adresse):
		if id_adresse in self._adresses:
			del self._adresses[id_adresse]

	adresses = property(adresses,ajouter_adresse)

	def batiments(self):
	    return self._batiments


	def ajouter_batiment(self,no_bat, nom, adresse):
		if no_bat not in self._batiments:
			nouveau_bat = batiment.Batiment(no_bat, nom, adresse)
			self._batiments[no_bat] = nouveau_bat


	batiments = property(batiments, ajouter_batiment)
	

	def rechercher_batiment(self, no_bat):
		if no_bat in self._batiments:
			return self._batiments[no_bat]


	def modifier_batiment(self, no_bat, nom, adresse):
		if no_bat in self._batiments:
			nouveau_bat = batiment.Batiment(no_bat, nom, adresse)
			self._batiments[no_bat] = nouveau_bat

	def supprimer_batiment(self, no_bat):
		if no_bat not in self._batiments:
			del self._batiments[no_bat]


	#fonctionnalitées typesalle
	def typesalles(self):
	    return self._typesalles

	def ajouter_typesalle(self, nom_typesalle, description):
		if nom_typesalle not in self._typesalles:
			nouveau_typesalle = typesalle.Typesalle(description)
			self._typesalles[nom_typesalle] = nouveau_typesalle

	def supprimer_typesalle(self, nom_typesalle):
		if nom_typesalle in self._typesalles:
			del self._typesalles[nom_typesalle]

	def consulter_typesalle(self, description):
		if nom_typesalle in self._typesalles:
			return self._typesalles[nom_typesalle]

	typesalles = property(typesalles, ajouter_typesalle)


	#fonctionnalitées materiel

	def materiels(self):
	    return self._materiels

	def ajouter_materiel(self, code_inv):
		if code_inv not in self._materiels:
			nouveau_materiel = materiel.Materiel(code_inv)
			self._materiels[code_inv] = nouveau_materiel

	def supprimer_materiel(self, code_inv):
		if code_inv in self._materiels:
			del self._materiels[code_inv]

	def consulter_materiel(self, code_inv):
		if code_inv in self._materiels:
			return self._materiels[code_inv]

	materiels = property(materiels,ajouter_materiel)
	#--------------------------------


	#fonctionnalitées typemateriel
	def typemateriels(self):
	    return self._typemateriels

	def ajouter_typemateriel(self, nom, code, libelle, montant):
		if nom not in self._typemateriels:
			nouveau_typemateriel = typemateriel.Typemateriel(nom, code, libelle, montant)
			self._typemateriels[nom] = nouveau_typemateriel

	def supprimer_typemateriel(self, nom):
		if nom in self._typemateriels:
			del self._typemateriels[nom]

	def consulter_typemateriel(self, nom):
		if nom in self._typemateriels:
			return self._typemateriels[nom]

	typemateriels = property(typemateriels,ajouter_typemateriel)

	#fonctionnalitées salle
	#fonction d'ajout d'une salle si le batiment ou le typesalle n'existe pas alors la fonction est abandonné


	def ajouter_salle(self, no_bat, no_etage, no_salle, superficie, nom_typesalle):
		if no_bat in self._batiments:
			if nom_typesalle in self._typesalles:
				self._batiments[no_bat].ajouter_salle(no_etage, no_salle, no_bat, superficie, nom_typesalle)

	#fonction pour supprimer une salle
	def supprimer_salle(self, no_bat, no_etage, no_salle):
		#for r in self._reservations:
			#if r in self._reservations:
		self._batiments[no_bat].supprimer_salle(no_bat, no_etage, no_salle)

	#-------------------------------

	#fonctionnalitées pour la classe demandeur
	def ajouter_demandeur(self, no_dem, nom):
		return 0


def main():

	systeme = GestionAPI()
	systeme.ajouter_batiment(1,"Batiment 1","Adresse 1")
	#systeme.supprimer_batiment(1)
	print (systeme.rechercher_batiment(1))
	systeme.ajouter_typemateriel("Télévision",1,"télévision",100)
	print (systeme.typemateriels)
	systeme.ajouter_typesalle("Classe","Cool description")
	systeme.ajouter_salle(1,1,1,10,"Classe")
	systeme.supprimer_salle(1,1,1)
	print(systeme.batiments)

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
