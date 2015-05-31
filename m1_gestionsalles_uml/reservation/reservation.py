import time
class Reservation(object):
	"""Classe représentant une réservation faite par un demandeur

	Attributs:
	ref_resa : référance pour une réservation
	date : date de la réservation 
	montant : montant de la réservation
	no_dem : numéro unique du demandeur
	id_salle : identifiant de la salle
	code_manifestation : manifestation lier à la réservation
	code_duree : durée de la réservation

	"""
	
	def __init__(self, ref_resa, date, no_dem, no_bat, no_etage, no_salle, code_manifestation, code_duree):
		super(Reservation, self).__init__()
		self.ref_resa = ref_resa
		self.date = time.strptime(date, "%d/%m/%Y")
		self.montant = 0
		self.no_dem = no_dem
		self.id_salle = str(no_bat)+" "+str(no_etage)+" "+str(no_salle)
		self.code_manifestation = code_manifestation
		self.code_duree = code_duree
		
	def __str__(self):
		return "{} {} {} {} {} {} {}".format(self.ref_resa ,time.strftime('%d/%m/%Y',self.date) ,self.montant ,self.no_dem ,self.id_salle, self.code_manifestation, self.code_duree)

	def __repr__(self):
		return "{} {} {} {} {} {} {}".format(self.ref_resa ,time.strftime('%d/%m/%Y',self.date) ,self.montant ,self.no_dem ,self.id_salle, self.code_manifestation, self.code_duree)

	@property
	def no_dem(self):
	    return self._no_dem

	@no_dem.setter
	def no_dem(self, val):
		self._no_dem = val

	@property
	def date(self):
	    return self._date

	@date.setter
	def date(self, val):
		self._date = val

	@property
	def no_dem(self):
	    return self._no_dem

	@no_dem.setter
	def no_dem(self, val):
		self._no_dem = val

	@property
	def montant(self):
	    return self._montant

	@montant.setter
	def montant(self,val):
		self._montant = val
	