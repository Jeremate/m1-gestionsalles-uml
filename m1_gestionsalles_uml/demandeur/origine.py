from finance.tabletarif import TableTarif

class Origine(TableTarif):
	"""Classe représentant l'origine d'un demandeur.

	Attributs:

	"""

	def __init__(self, code, libelle, montant):
		super(Origine, self).initialisation(code, libelle, montant)
