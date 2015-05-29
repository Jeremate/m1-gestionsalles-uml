from finance.tabletarif import TableTarif

class Origine(TableTarif):
	"""Classe représentant l'origine d'un demandeur.

	Attributs:
		nom : Le nom de l'origine
	"""

	def __init__(self, nom , code, libelle, montant):
		super(Typemateriel, self).initialisation(code, libelle, montant)
		self.nom

	def __str__(self):
		return "{}".format(self.nom)

	def __repr__(self):
		return "{}".format(self.nom)

	@property
	def nom(self):
	    return self._nom

	@nom.setter
	def nom(self, val):
		self._nom = val