from finance.tabletarif import TableTarif

class Titre(TableTarif):
	"""Classe représentant le titre d'un demandeur.

	Attributs:

	"""

	def __init__(self, code, libelle, montant):
		super(Titre, self).initialisation(code, libelle, montant)
		