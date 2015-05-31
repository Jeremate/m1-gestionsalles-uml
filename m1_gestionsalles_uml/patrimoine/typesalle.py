from finance.tabletarif import TableTarif

class TypeSalle(TableTarif):
	"""Classe représentant un type de salle.

	Attributs:
	"""

	def __init__(self, code, libelle, montant):
		super(TypeSalle, self).initialisation(code, libelle, montant)