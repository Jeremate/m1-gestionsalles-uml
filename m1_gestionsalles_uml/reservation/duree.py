from finance.tabletarif import TableTarif

class Duree(TableTarif):
	"""Classe représentant la durée liée a une réservation

	Attributs:

	"""

	def __init__(self, code, libelle, montant):
		super(Duree, self).initialisation(code, libelle, montant)
