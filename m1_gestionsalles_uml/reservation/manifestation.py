from m1_gestionsalles_uml.finance.tabletarif import TableTarif

class Manifestation(TableTarif):
	"""Classe représentant une manifestation liée a une réservation

	Attributs:

	"""

	def __init__(self, code, libelle, montant):
		super(Manifestation, self).initialisation(code, libelle, montant)
