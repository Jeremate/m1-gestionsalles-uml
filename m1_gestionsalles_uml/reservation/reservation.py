class Reservation(object):
	"""Classe représentant une réservation faite par un demandeur

	Attributs:


	"""
	
	def __init__(self, ref, date, montant, no_dem, id_salle):
		super(Reservation, self).__init__()
		self.ref_resa = ref
		self.date = date
		self.montant = montant
		self.demandeur = no_dem
		self.salle = id_salle
		
	