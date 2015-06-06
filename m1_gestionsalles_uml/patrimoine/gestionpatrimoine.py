from patrimoine.batiment import Batiment
from patrimoine.materiel import Materiel
from patrimoine.typemateriel import TypeMateriel
from patrimoine.typesalle import TypeSalle
from patrimoine.salle import Salle
from localisation.gestionlocalisation import GestionLocalisation

class GestionPatrimoine(object):

	__instance = None
	def __new__(cls):
		if GestionPatrimoine.__instance is None:
			GestionPatrimoine.__instance = object.__new__(cls)
			GestionPatrimoine.__instance._batiments = {}
			GestionPatrimoine.__instance._materiels = {}
			GestionPatrimoine.__instance._typemateriels = {}
			GestionPatrimoine.__instance._salles = {}
			GestionPatrimoine.__instance._typesalles = {}
			GestionPatrimoine.__instance._materiels = GestionLocalisation()
		return GestionPatrimoine.__instance


	def materiels(self):
		return GestionPatrimoine.__instance._materiels

	materiels = property(materiels)


	#fonctionnalitées batiment
	def batiments(self):
	    return GestionPatrimoine.__instance._batiments

	def ajouter_batiment(self,no_bat, nom, adresse):
		if no_bat not in self.batiments:
			self.batiments[no_bat] = Batiment(no_bat, nom, adresse)

	batiments = property(batiments)

	def rechercher_batiment(self, no_bat):
		if no_bat in self.batiments:
			return self.batiments[no_bat]


	def modifier_batiment(self, no_bat, nom, adresse):
		if no_bat in self.batiments:
			self.batiments[no_bat] = Batiment(no_bat, nom, adresse)

	def supprimer_batiment(self, no_bat):
		if no_bat not in self.batiments:
			del self.batiments[no_bat]
	#------------------------------------

	#fonctionnalitées typesalle
	def typesalles(self):
	    return GestionPatrimoine.__instance._typesalles

	def ajouter_typesalle(self, code, libelle, montant):
		if code not in self.typesalles:
			self.typesalles[code] = TypeSalle(code, libelle, montant)

	def supprimer_typesalle(self, code):
		if code in self.typesalles:
			del self.typesalles[code]

	def consulter_typesalle(self, code):
		if code in self.typesalles:
			return self.typesalles[code]

	typesalles = property(typesalles)

	#fonctionnalitées materiel

	def materiels(self):
	    return GestionPatrimoine.__instance._materiels

	def ajouter_materiel(self, code_inv, libelle, montant):
		if code_inv not in self.materiels:
			self.materiels[code_inv] = Materiel(code_inv)

	def supprimer_materiel(self, code_inv):
		if code_inv in self.materiels:
			del self.materiels[code_inv]

	def consulter_materiel(self, code_inv):
		if code_inv in self.materiels:
			return self.materiels[code_inv]

	materiels = property(materiels)
	#--------------------------------

	#fonctionnalitées typemateriel
	def typemateriels(self):
	    return GestionPatrimoine.__instance._typemateriels

	def ajouter_typemateriel(self, code, libelle, montant):
		if code not in self.typemateriels:
			self.typemateriels[code] = TypeMateriel(code, libelle, montant)

	def supprimer_typemateriel(self, nom):
		if nom in self.typemateriels:
			del self.typemateriels[nom]

	def consulter_typemateriel(self, nom):
		if nom in self.typemateriels:
			return self.typemateriels[nom]

	typemateriels = property(typemateriels)


	#fonctionnalitées salle
	#fonction d'ajout d'une salle si le batiment ou le typesalle n'existe pas alors la fonction est abandonné
	def associer_materiel(self, no_bat, no_etage, no_salle, code_inv):
		if no_bat in self.batiments:
			if code_inv in self.materiels:
				self._batiments[no_bat].associer_materiel(no_bat, no_etape, no_salle, code_inv, self._materiels[code_inv])


	def salles(self):
		return GestionPatrimoine.__instance._salles

	def ajouter_salle(self, no_bat, no_etage, no_salle, superficie, nom_typesalle):
		if no_bat in self.batiments:
			if nom_typesalle in self.typesalles:
				self.batiments[no_bat].ajouter_salle(no_etage, no_salle, no_bat, superficie, nom_typesalle)

	#fonction pour supprimer une salle
	def supprimer_salle(self, no_bat, no_etage, no_salle):
		if no_bat in self.batiments:
			#for r in self._reservations:
				#if r in self._reservations:
			self.batiments[no_bat].supprimer_salle(no_bat, no_etage, no_salle)

	salles = property(salles)
	#-------------------------------
