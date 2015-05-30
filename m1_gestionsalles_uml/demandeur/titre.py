from finance.tabletarif import TableTarif

class Titre(Tabletarif):
	"""Classe représentant le titre d'un demandeur.

	Attributs:
		id_titre ; identifiant du titre d'un demandeur
	"""

	def __init__(self, id_titre , code, libelle, montant):
		super(Typemateriel, self).initialisation(code, libelle, montant)
		self.id_titre = id_titre


	def __str__(self):
		return "{}".format(self.id_titre)

	def __repr__(self):
		return self._id_titre

	@property
	def id_titre(self):
	    return self._id_titre

	@id_titre.setter
	def id_titre(self, val):
		self._id_titre = val