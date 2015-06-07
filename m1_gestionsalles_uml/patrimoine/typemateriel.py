from m1_gestionsalles_uml.finance.tabletarif import TableTarif

class TypeMateriel(TableTarif):
	"""Classe représentant un type de materiel.

	"""

	def __init__(self, code, libelle, montant):
		super(TypeMateriel, self).initialisation(code, libelle, montant)

