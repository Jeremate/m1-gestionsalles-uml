from finance.tabletarif import TableTarif

class Typemateriel(TableTarif):
	"""Classe représentant un type de materiel.

	"""

	def __init__(self, nom , code, libelle, montant):
		super(Typemateriel, self).initialisation(code, libelle, montant)

