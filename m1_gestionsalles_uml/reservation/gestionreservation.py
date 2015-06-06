from reservation.reservation import Reservation
from reservation.manifestation import Manifestation
from reservation.duree import Duree
from patrimoine.gestionpatrimoine import GestionPatrimoine
from demandeur.gestiondemandeur import GestionDemandeur

class GestionReservation(object):

	__instance = None
	def __new__(cls):
		if GestionReservation.__instance is None:
			GestionReservation.__instance = object.__new__(cls)
			GestionReservation.__instance._reservations = {}
			GestionReservation.__instance._manifestations = {}
			GestionReservation.__instance._durees = {}
			GestionReservation.__instance._batiments = GestionPatrimoine()
			GestionReservation.__instance._typesalles = GestionPatrimoine()
			GestionReservation.__instance._typemateriels = GestionPatrimoine()
			GestionReservation.__instance._origines = GestionDemandeur()
			GestionReservation.__instance._demandeurs = GestionDemandeur()
			GestionReservation.__instance._titres= GestionDemandeur()
		return GestionReservation.__instance


	def batiments(self):
		return GestionReservation.__instance._batiments.batiments

	batiments = property(batiments)

	def typesalles(self):
		return GestionReservation.__instance._typesalles.typesalles

	typesalles = property(typesalles)

	def typemateriels(self):
		return GestionReservation.__instance._typemateriels.typemateriels

	typemateriels = property(typemateriels)

	def origines(self):
		return GestionReservation.__instance._origines.origines

	origines = property(origines)

	def titres(self):
		return GestionReservation.__instance._titres.titres

	titres = property(titres)

	def demandeurs(self):
		return GestionReservation.__instance._demandeurs.demandeurs

	demandeurs = property(demandeurs)

	#fonctionnalitées pour la classe réservation
	def reservations(self):
		return GestionReservation.__instance._reservations

	def calculer_montant(self, ref_resa):
		res = 0
		liste_salle = self.batiments[self._reservations[ref_resa].no_bat].salles
		for salle in liste_salle:
			res = res + self.typesalles[liste_salle[salle].typesalle].montant
			liste_mat = liste_salle[salle].materiels
			for mat in liste_mat:
				res = res + self.typemateriels[liste_mat[mat].typemateriel].montant
		res = res + self.origines[self._demandeurs[self._reservations[ref_resa].no_dem].origine].montant
		res = res + self.titres[self._demandeurs[self._reservations[ref_resa].no_dem].titre].montant
		res = res + self.manifestations[self._reservations[ref_resa].code_manifestation].montant
		res = res + self.durees[self._reservations[ref_resa].code_duree].montant
		self.reservations[ref_resa].montant = res

	def ajouter_reservation(self, ref_resa, date, no_dem, no_bat, no_etage, no_salle, code_manifestation, code_duree):
		if ref_resa not in self.reservations:	
			if no_bat in self.batiments:
				if code_manifestation in self.manifestations:
					if code_duree in self._durees:
						if self.batiments[no_bat].salle_presente(no_bat, no_etage, no_salle):
							self.reservations[ref_resa] = Reservation(ref_resa, date, no_dem, no_bat, no_etage, no_salle, code_manifestation, code_duree)
							self.calculer_montant(ref_resa)

	def consulter_reservation(self, ref_resa):
		if ref_resa in self.reservations:
			return self.reservations[ref_resa]

	reservations = property(reservations)
	#----------------------------------------

	#fonctionnalitées manifestation
	def manifestations(self):
		return GestionReservation.__instance._manifestations

	def ajouter_manifestation(self, code, libelle, montant):
		if code not in self.manifestations:
			self.manifestations[code] = Manifestation(code, libelle, montant)

	def supprimer_manifestation(self, code):
		if code in self.manifestations:
			del self.manifestations[code]

	manifestations = property(manifestations)

	#fonctionnalitées durees
	def durees(self):
		return GestionReservation.__instance._durees

	def ajouter_duree(self, code, libelle, montant):
		if code not in self.durees:
			self.durees[code] = Duree(code, libelle, montant)

	def supprimer_duree(self, code):
		if code in self._durees:
			del self._durees[code]

	durees = property(durees)
