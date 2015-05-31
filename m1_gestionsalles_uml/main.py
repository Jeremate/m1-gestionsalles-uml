from patrimoine import batiment
from patrimoine.typesalle import TypeSalle
from patrimoine import materiel
from patrimoine.typemateriel import TypeMateriel
from patrimoine import salle
from finance.tabletarif import TableTarif
from localisation.adresse import Adresse
from demandeur.titre import Titre
from demandeur.origine import Origine
from demandeur.demandeur import Demandeur
from reservation.reservation import Reservation
from reservation.manifestation import Manifestation
from reservation.duree import Duree

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
		self._demandeurs = {}
		self._reservations = {}
		self._origines = {}
		self._titres = {}
		self._durees = {}
		self._manifestations = {}
		self._adresses = {}



	def adresses(self):
		return self._adresses

	def ajouter_adresse(self, id_adresse, no, adresse, code, ville):
		if id_adresse not in self._adresses:
			self._adresses[id_adresse] = Adresse(no, adresse, code, ville)

	def supprimer_adresse(self, id_adresse):
		if id_adresse in self._adresses:
			del self._adresses[id_adresse]

	adresses = property(adresses,ajouter_adresse)

	def titres(self):
		return self._titres

	def ajouter_titre(self, code, libelle, montant):
		if code not in self._titres:
			self._titres[code] = Titre(code, libelle, montant)

	def supprimer_titre(self, code):
		if code in self._titres:
			del self._titres[code]

	titres = property(titres, ajouter_titre)

	def manifestations(self):
		return self._manifestations

	def ajouter_manifestation(self, code, libelle, montant):
		if code not in self._manifestations:
			self._manifestations[code] = Manifestation(code, libelle, montant)

	def supprimer_manifestation(self, code):
		if code in self._manifestations:
			del self._manifestations[code]

	manifestations = property(manifestations, ajouter_titre)


	def durees(self):
		return self._durees

	def ajouter_duree(self, code, libelle, montant):
		if code not in self._durees:
			self._durees[code] = Duree(code, libelle, montant)

	def supprimer_duree(self, code):
		if code in self._durees:
			del self._durees[code]

	durees = property(durees, ajouter_titre)

	def origines(self):
		return self._origines

	def ajouter_origine(self, code, libelle, montant):
		if code not in self._origines:
			self._origines[code] = Origine(code, libelle, montant)

	def supprimer_origine(self, code):
		if code in self._origines:
			del self._origines[code]

	origines = property(origines,ajouter_origine)

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

	def ajouter_typesalle(self, code, libelle, montant):
		if code not in self._typesalles:
			self._typesalles[code] = TypeSalle(code, libelle, montant)

	def supprimer_typesalle(self, code):
		if code in self._typesalles:
			del self._typesalles[code]

	def consulter_typesalle(self, code):
		if code in self._typesalles:
			return self._typesalles[code]

	typesalles = property(typesalles, ajouter_typesalle)


	#fonctionnalitées materiel

	def materiels(self):
	    return self._materiels

	def ajouter_materiel(self, code_inv, libelle, montant):
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

	def ajouter_typemateriel(self, code, libelle, montant):
		if code not in self._typemateriels:
			self._typemateriels[code] = TypeMateriel(code, libelle, montant)

	def supprimer_typemateriel(self, nom):
		if nom in self._typemateriels:
			del self._typemateriels[nom]

	def consulter_typemateriel(self, nom):
		if nom in self._typemateriels:
			return self._typemateriels[nom]

	typemateriels = property(typemateriels,ajouter_typemateriel)

	#fonctionnalitées salle
	#fonction d'ajout d'une salle si le batiment ou le typesalle n'existe pas alors la fonction est abandonné
	def associer_materiel(self, no_bat, no_etage, no_salle, code_inv):
		if no_bat in self._batiments:
			if code_inv in self._materiels:
				self._batiments[no_bat].associer_materiel(no_bat, no_etape, no_salle, code_inv, self._materiels[code_inv])

	def salles(self):
		return self._salles

	def ajouter_salle(self, no_bat, no_etage, no_salle, superficie, nom_typesalle):
		if no_bat in self._batiments:
			if nom_typesalle in self._typesalles:
				self._batiments[no_bat].ajouter_salle(no_etage, no_salle, no_bat, superficie, nom_typesalle)

	#fonction pour supprimer une salle
	def supprimer_salle(self, no_bat, no_etage, no_salle):
		if no_bat in self._batiments:
			#for r in self._reservations:
				#if r in self._reservations:
			self._batiments[no_bat].supprimer_salle(no_bat, no_etage, no_salle)

	salles = property(salles, ajouter_salle)
	#-------------------------------

	#fonctionnalitées pour la classe demandeur
	def demandeurs(self):
		return self._demandeurs

	def ajouter_demandeur(self, no_dem, nom, id_adresse, nom_origine, id_titre):
		if no_dem not in self._demandeurs:
			if nom_origine in self._origines:
				if id_titre in self._titres:
					if id_adresse in self._adresses:
						self._demandeurs[no_dem] = Demandeur(no_dem, nom , id_adresse, nom_origine, id_titre)

	def supprimer_demandeur(self, no_dem):
		if no_dem in self._demandeurs:
			del self._demandeurs[no_dem]

	demandeurs = property(demandeurs, ajouter_demandeur)
	#--------------------------------

	#fonctionnalitées pour la classe réservation
	def reservations(self):
		return self._reservations

	def calculer_montant(self, ref_resa):
		self._reservations[ref_resa].montant = 10

	def ajouter_reservation(self, ref_resa, date, no_dem, no_bat, no_etage, no_salle, code_manifestation, code_duree):
		if ref_resa not in self._reservations:	
			if no_bat in self._batiments:
				if self._batiments[no_bat].salle_presente(no_bat, no_etage, no_salle):
					self._reservations[ref_resa] = Reservation(ref_resa, date, no_dem, no_bat, no_etage, no_salle, code_manifestation, code_duree)
					self.calculer_montant(ref_resa)

	def consulter_reservation(self, ref_resa):
		if ref_resa in self._reservations:
			return self._reservations[ref_resa]

	reservations = property(reservations, ajouter_reservation)

	
	#----------------------------------------

def main():

	systeme = GestionAPI()
	systeme.ajouter_adresse("Adresse 1", 10, "Rue des Landes", "44300", "Nantes")
	systeme.ajouter_batiment(1,"Batiment 1","Adresse 1")
	#systeme.supprimer_batiment(1)
	#print (systeme.rechercher_batiment(1))
	systeme.ajouter_typemateriel("Télévision","télévision HD LCD",100)
	print (systeme.typemateriels)
	systeme.ajouter_typesalle("Classe", "salle de classe", 200)
	systeme.ajouter_salle(1,1,1,10,"Classe")
	#systeme.supprimer_salle(1,1,1)
	print(systeme.batiments)
	systeme.associer_materiel(1,1,1,"Télévision")
	systeme.ajouter_origine("Resident","résident",100)
	systeme.ajouter_titre("Etudiant", "Etudiant", 100)
	systeme.ajouter_demandeur(1, "Boceno", "Adresse 1", "Resident", "Etudiant")
	print(systeme.demandeurs)
	systeme.ajouter_reservation(1, "31/05/2015", 1, 1, 1, 1, 1, 1)
	print(systeme.reservations)

if __name__ == '__main__':
	main()
